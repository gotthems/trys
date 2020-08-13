
from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from advirtise.views import AdvirtisetViewset

router = DefaultRouter()
router.register(r'advirtise', AdvirtisetViewset)

urlpatterns = [
   path('', include(router.urls))
]