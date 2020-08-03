from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from vuenote.models import Note
from vuenote.serializers import NoteSerializer,DeleteSerializer,UpdateSerializer


# Create your views here.


class NoteViewSet(viewsets.ModelViewSet):
    """permission_classes = {
        IsAuthenticated
    }"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'


class DeleteDemand(DestroyAPIView):
    serializer_class = DeleteSerializer
    queryset = Note.objects.all()
    lookup_field = 'id'


class UpdateDemand(UpdateAPIView):
    serializer_class = UpdateSerializer
    queryset = Note.objects.all()
    lookup_field = 'id'