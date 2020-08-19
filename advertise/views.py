from django.http import Http404, request
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, UpdateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.serializers import ModelSerializer, StringRelatedField
from advertise.models.advertise_main_model import *
from advertise.serializer.AdvirtiseMainSerializer import AdvertiseMainSerializer, GetAdvertiseMainSerializer
from django.views.generic import ListView, DetailView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User


def images(request):
    Advertise.user = request.user
    image = AdvertiseImage.objects.all()
    mod = Advertise.objects.all()
    return render(request, 'x.html', context={'image': image, 'mod': mod})


# İlan modeli oluşturma
class CreateAdvertiseView(CreateAPIView):
    serializer_class = AdvertiseMainSerializer
    queryset = Advertise.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Tüm İlan modellerini görüntüleme
class AllAdvertiseListView(ListAPIView):
    serializer_class = GetAdvertiseMainSerializer
    queryset = Advertise.objects.all()


# Sadece İlan sahibine ait ilan modellerini görüntüleme
class UserOwnedAdvertiseData(APIView):
    @staticmethod
    def get(request):
        allposts = Advertise.objects.filter(owner=request.user)
        serializer = GetAdvertiseMainSerializer(allposts, many=True)
        return Response(serializer.data)


# İlan sahibine ait ilan modellini güncelleme
class UpdateAdvertiseData(RetrieveUpdateAPIView):
    serializer_class = AdvertiseMainSerializer
    queryset = Advertise.objects.all()

    def get_queryset(self):
        return self.queryset.model.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# İlan sahibine ait ilan modellini silme
class DeleteAdvertiseData(RetrieveDestroyAPIView):
    serializer_class = AdvertiseMainSerializer
    queryset = Advertise.objects.all()

    def get_queryset(self):
        return self.queryset.model.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
