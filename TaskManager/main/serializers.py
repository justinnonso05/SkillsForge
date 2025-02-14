from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.utils.timezone import now

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "category", "completed", "due_date", "created_at"]

    def validate_due_date(self, value):
        if value and value < now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value