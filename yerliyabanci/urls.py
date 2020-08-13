"""yerliyabanci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from advirtise import urls
from user import urls
from vuenote.views import DeleteDemand,UpdateDemand
from vuenote.views import sendmodel
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('api', include('vuenote.urls')),
    url(r'^delete/(?P<id>[-\w]+)/$', DeleteDemand.as_view()),
    url(r'^update/(?P<id>[-\w]+)/$', UpdateDemand.as_view()),
    url(r'api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include(urls)),
    path('advirtise/',include('advirtise.urls'))
]

"""urlpatterns += [
    re_path('', TemplateView.as_view(template_name="index.html")),
]"""

"""path('sendmodel/', sendmodel, name='sendmodel'),

"""