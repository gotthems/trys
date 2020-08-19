from django.db import models

# Create your models here.

from advertise.choices.AdvirtiseChoices import (NumberOfRoomsChoices, NumberOfBuildingAgeChoices, NumberOfFloorChoices,
                                                NumberOfBathroomsChoices,
                                                HeatingChoices, UsingStatusChoices, AdvertiseStatusChocies,
                                                AdvertiseVisibilityChoices, HousingShapeChoices)
from user.models import User


class Advertise(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, verbose_name="ilan başlığı")
    description = models.TextField(max_length=500, verbose_name="ilan açıklaması")
    price = models.PositiveIntegerField(default=0, verbose_name="Fiyat")
    square_meter = models.PositiveIntegerField(default=0, verbose_name="Metrekaresi")
    number_of_rooms = models.PositiveIntegerField(choices=NumberOfRoomsChoices.CHOICES, verbose_name="Oda sayısı")
    building_age = models.PositiveIntegerField(choices=NumberOfBuildingAgeChoices.CHOICES, verbose_name="Bina Yaşı")
    floor = models.PositiveIntegerField(choices=NumberOfFloorChoices.FLOOR_CHOICES, verbose_name="Bulunduğu Kat")
    number_of_floors = models.PositiveIntegerField(choices=NumberOfFloorChoices.FLOORS_CHOICES,
                                                   verbose_name="Kat sayısı")
    number_of_bathrooms = models.PositiveIntegerField(choices=NumberOfBathroomsChoices.CHOICES,
                                                      verbose_name="banyo sayısı")
    heating = models.PositiveIntegerField(choices=HeatingChoices.CHOICES, verbose_name="Isınma Durumu")
    balcony_exists = models.BooleanField(default=False, verbose_name="Balkon Durumu")
    using_status = models.PositiveIntegerField(choices=UsingStatusChoices.CHOICES, verbose_name="Kullanım Durumu")
    housing_shape = models.PositiveIntegerField(choices=HousingShapeChoices.CHOICES, verbose_name="Konut Şekli")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="İlan oluşturma zamanı")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="ilan güncellenme zamanı")
    status = models.PositiveIntegerField(choices=AdvertiseStatusChocies.CHOICES, verbose_name="Aktiflik Durumu")
    visibility = models.PositiveIntegerField(choices=AdvertiseVisibilityChoices.CHOICES,
                                             verbose_name="İlan Görünürlüğü")
    image = models.ImageField(blank=True)

    # collections
    frontal = models.ManyToManyField(to="advertise.Frontal")
    interior_feature = models.ManyToManyField(to="advertise.InteriorFeature")
    exterior_feature = models.ManyToManyField(to="advertise.ExteriorFeature")
    locality = models.ManyToManyField(to="advertise.Locality")
    transportation = models.ManyToManyField(to="advertise.Transportation")
    landscape = models.ManyToManyField(to="advertise.Landscape")
    sutiable_for_disabled = models.ManyToManyField(to="advertise.SuitableForDisabled")

    def __str__(self):
        return f"{self.title}"




class AdvertiseImage(models.Model):
    advertiseForeign = models.ForeignKey(Advertise, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/', blank=True)

    def __str__(self):
        return self.advertiseForeign.title

    @property
    def image_url(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url

