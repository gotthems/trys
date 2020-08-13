from django.shortcuts import render
from rest_framework import viewsets
from advirtise.serializers import *
from advirtise.models import *
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.


class AdvirtisetViewset(viewsets.ModelViewSet):
    queryset = Advertise.objects.all()
    serializer_class = AdvirtiseSerializer
    lookup_field = 'id'
