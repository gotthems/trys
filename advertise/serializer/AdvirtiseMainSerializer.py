from rest_auth import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField, SerializerMethodField, ReadOnlyField
from advertise.models.advertise_main_model import Advertise


class AdvertiseMainSerializer(ModelSerializer):
    class Meta:
        model = Advertise
        fields = '__all__'


class ChoicesSerializerField(SerializerMethodField):
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


class GetAdvertiseMainSerializer(ModelSerializer):
    frontal = StringRelatedField(many=True)
    locality = StringRelatedField(many=True)
    interior_feature = StringRelatedField(many=True)
    exterior_feature = StringRelatedField(many=True)
    transportation = StringRelatedField(many=True)
    landscape = StringRelatedField(many=True)
    sutiable_for_disabled = StringRelatedField(many=True)
    status = ChoicesSerializerField(choices=Advertise.status)
    number_of_rooms = ChoicesSerializerField(choices=Advertise.number_of_rooms)
    building_age = ChoicesSerializerField(choices=Advertise.building_age)
    floor = ChoicesSerializerField(choices=Advertise.floor)
    number_of_floors = ChoicesSerializerField(choices=Advertise.number_of_floors)
    number_of_bathrooms = ChoicesSerializerField(choices=Advertise.number_of_bathrooms)
    heating = ChoicesSerializerField(choices=Advertise.heating)
    using_status = ChoicesSerializerField(choices=Advertise.using_status)
    housing_shape = ChoicesSerializerField(choices=Advertise.housing_shape)
    visibility = ChoicesSerializerField(choices=Advertise.visibility)

    # güncelleme yapamadığım için Bilgileri görüntülemek için kullanmak istediğim serializer modelinde kullanacağım

    class Meta:
        model = Advertise
        fields = '__all__'
