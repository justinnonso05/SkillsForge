from django.urls import path
from .views import TaskList, TaskCreate, TaskRetrieve, TaskUpdate, TaskDelete, UserLoginView, UserSignupView, TaskOverdue
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("auth/login/", UserLoginView.as_view(), name="login_user"),
    path("auth/signup/", UserSignupView.as_view(), name="signup_user"),

    path("api/tasks/list", TaskList.as_view(), name="list_tasks"),
    path("api/tasks/overdue", TaskOverdue.as_view(), name="overdue_tasks"),
    path("api/tasks/create", TaskCreate.as_view(), name="create_tasks"),
    path("api/tasks/<str:pk>/", TaskRetrieve.as_view(), name="retrieve_task"),
    path("api/tasks/<str:pk>/update/", TaskUpdate.as_view(), name="update_task"),
    path("api/tasks/<str:pk>/delete/", TaskDelete.as_view(), name="delete_task"),

    # Spectacular Schema & Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]


''' Remove refresh token and make the access token last longer 
    Create a nother super user with more specific login details
'''