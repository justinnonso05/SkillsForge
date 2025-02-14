from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from django.utils.timezone import now
from .schemas import (
    signup_schema, 
    login_schema, 
    task_list_schema, 
    task_create_schema, 
    task_retrieve_schema,
    task_update_schema, 
    task_delete_schema,
    task_overdue_schema
)

class UserSignupView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    @signup_schema
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, password=password)
            return Response({
                'message': f"User {user.username} created successfully. Please log in to get your tokens."
            }, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'auth_user.username' in str(e):
                return Response({"error": "A user with this username already exists."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "An unknown error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    @login_schema
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'username': user.username
                }
            })
        else:
            return Response({'error': 'Invalid credentials'}, 
                status=status.HTTP_401_UNAUTHORIZED)


class TaskListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TaskList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    @task_list_schema
    def get(self, request, format=None):
        tasks = Task.objects.filter(user=request.user)
        category_query = request.query_params.get('category', None)
        search_query = request.query_params.get('search', None)

        if search_query:
            tasks = tasks.filter(Q(title__icontains=search_query.upper()))
        if category_query:
            tasks = tasks.filter(category=category_query)

        paginator = TaskListPagination()
        paginated_tasks = paginator.paginate_queryset(tasks, request, view=self)
        serializer = TaskSerializer(paginated_tasks, many=True)
        return paginator.get_paginated_response(serializer.data)


class TaskOverdue(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    @task_overdue_schema
    def get(self, request, format=None):
        overdue_tasks = Task.objects.filter(user=request.user, due_date__lt=now(), completed=False)
        category_query = request.query_params.get('category', None)
        search_query = request.query_params.get('search', None)

        if search_query:
            overdue_tasks = overdue_tasks.filter(Q(title__icontains=search_query.upper()))
        if category_query:
            overdue_tasks = overdue_tasks.filter(category=category_query)

        paginator = TaskListPagination()
        paginated_tasks = paginator.paginate_queryset(overdue_tasks, request, view=self)
        serializer = TaskSerializer(paginated_tasks, many=True)

        # Create a modified list including overdue time
        modified_tasks = []
        for task in serializer.data:
            due_date = Task.objects.get(id=task['id']).due_date
            overdue_time = now() - due_date
            overdue_info = {
                'hours': int(overdue_time.total_seconds() // 3600),
                'minutes': int((overdue_time.total_seconds() % 3600) // 60)
            }

            # Append a modified task dictionary with `overdue_by`
            modified_task = dict(task)  # Convert OrderedDict to a mutable dict
            modified_task['overdue_by'] = overdue_info
            modified_tasks.append(modified_task)

        response_data = {
            'message': 'These tasks are overdue.',
            'tasks': modified_tasks
        }
        return paginator.get_paginated_response(response_data)


class TaskCreate(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    @task_create_schema
    def post(self, request, pk=None, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieve(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    @task_retrieve_schema
    def get(self, request, pk=None):
        try:
            task = Task.objects.get(id=pk, user=request.user)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have the required permissions to view the task."}, status=status.HTTP_404_NOT_FOUND)


class TaskUpdate(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    @task_update_schema
    def patch(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have the required permissions to view the task."}, status=status.HTTP_404_NOT_FOUND)


class TaskDelete(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    @task_delete_schema
    def delete(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            task.delete()
            return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have the required permissions to delete the task."}, status=status.HTTP_404_NOT_FOUND)
