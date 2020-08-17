from django.http import request
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from rest_auth.serializers import *
from user.choices.choice import GenderChoices

class ChoicesSerializerField(serializers.SerializerMethodField):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesSerializerField, self).__init__(**kwargs)

    def to_representation(self, value):
        # sample: 'get_XXXX_display'
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        # retrieve instance method
        method = getattr(value, method_name)
        # finally use instance method to return result of get_XXXX_display()
        return method()

    def to_internal_value(self, data):
        return getattr(self._choices, data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class UserSerializers(serializers.ModelSerializer):
    gender = ChoicesSerializerField(choices=User.gender)
    martial_status = ChoicesSerializerField(choices=User.martial_status)
    educational_status = ChoicesSerializerField(choices=User.educational_status)
    profession = ChoicesSerializerField(choices=User.profession)
    class Meta:
        model = User
        fields = "__all__"



class useSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'








