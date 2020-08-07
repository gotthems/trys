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
from vuenote.views import DeleteDemand,UpdateDemand

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"^.*$", TemplateView.as_view(template_name="index.html")),
    path('api', include('vuenote.urls')),
    url(r'^delete/(?P<id>[-\w]+)/$', DeleteDemand.as_view()),
    url(r'^update/(?P<id>[-\w]+)/$', UpdateDemand.as_view()),

]
urlpatterns += [
    re_path('^.*$', TemplateView.as_view(template_name="index.html")),
]