from django.shortcuts import render
from .serializers import TodoSerializers, UserSerializers
from rest_framework import viewsets
from todo.models import Todo
from django.contrib.auth.models import User

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializers

    def get_queryset(self):
        return Todo.objects.all().order_by("-created")


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.all().order_by("-date_joined")
