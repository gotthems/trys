from django.shortcuts import render

from rest_framework import generics
from user.serializer import UserSerializer
from .models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



"""class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer"""