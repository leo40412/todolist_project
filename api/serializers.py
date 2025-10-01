from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth.models import User


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
