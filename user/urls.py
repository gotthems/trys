from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from user.views import *




urlpatterns = [

    url(r'^rest-auth/', include('rest_auth.urls')),


]

"""path('user/', UserListView.as_view()),
 path('create/', CreateUserView.as_view()),"""