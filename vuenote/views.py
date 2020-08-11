import json

from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status, generics
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from vuenote.models import Note
from vuenote.serializers import NoteSerializer,DeleteSerializer,UpdateSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.


class NoteViewSet(viewsets.ModelViewSet):
    """permission_classes = {
        IsAuthenticated
    }"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content')

class DeleteDemand(DestroyAPIView):
    serializer_class = DeleteSerializer
    queryset = Note.objects.all()
    lookup_field = 'id'


class UpdateDemand(UpdateAPIView):
    serializer_class = UpdateSerializer
    queryset = Note.objects.all()
    lookup_field = 'id'


class NoteLookUp(viewsets.ModelViewSet):
    """permission_classes = {
        IsAuthenticated
    }"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('title','content')


def sendmodel(request):
    all_pro = Note.objects.all()
    data = serializers.serialize('json', all_pro, fields=('id','title','solved','software_lang','created_time'))
    return HttpResponse(data, content_type='application/json')


"""class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer"""