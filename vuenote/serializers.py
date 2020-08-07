from rest_framework import serializers, mixins, generics
from rest_framework.serializers import ModelSerializer

from vuenote.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class DeleteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class UpdateSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

