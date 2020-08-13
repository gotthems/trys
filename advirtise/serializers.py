from rest_framework import serializers, mixins, generics
from rest_framework.serializers import ModelSerializer
from advirtise.models import Advertise


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

class AdvirtiseSerializer(ModelSerializer):
    number_of_rooms = ChoicesSerializerField(choices=Advertise.number_of_rooms)
    building_age = ChoicesSerializerField(choices=Advertise.building_age)
    floor = ChoicesSerializerField(choices=Advertise.floor)
    number_of_floors = ChoicesSerializerField(choices=Advertise.number_of_floors)
    number_of_bathrooms = ChoicesSerializerField(choices=Advertise.number_of_bathrooms)
    heating = ChoicesSerializerField(choices=Advertise.heating)
    using_status = ChoicesSerializerField(choices=Advertise.using_status)
    status = ChoicesSerializerField(choices=Advertise.status)
    visibility = ChoicesSerializerField(choices=Advertise.visibility)



    class Meta:
        model = Advertise
        fields = "__all__"




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

class AdvirtiseSerializer(ModelSerializer):
    number_of_rooms = ChoicesSerializerField(choices=Advertise.number_of_rooms)
    building_age = ChoicesSerializerField(choices=Advertise.building_age)
    floor = ChoicesSerializerField(choices=Advertise.floor)
    number_of_floors = ChoicesSerializerField(choices=Advertise.number_of_floors)
    number_of_bathrooms = ChoicesSerializerField(choices=Advertise.number_of_bathrooms)
    heating = ChoicesSerializerField(choices=Advertise.heating)
    using_status = ChoicesSerializerField(choices=Advertise.using_status)
    status = ChoicesSerializerField(choices=Advertise.status)
    visibility = ChoicesSerializerField(choices=Advertise.visibility)



    class Meta:
        model = Advertise
        fields = "__all__"