import json

from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect,reverse

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
    data = serializers.serialize('json', all_pro, fields=('title'))
    return HttpResponse(data, content_type='application/json')
