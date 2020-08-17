from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import render
from requests import Response
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from user.serializer import *
from .models import *
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, get_object_or_404


class CreateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer













