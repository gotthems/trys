from django.conf.urls import url
from django.urls import include, path
from advertise.views import CreateAdvertiseView, images, AllAdvertiseListView, UserOwnedAdvertiseData,\
    UpdateAdvertiseData, DeleteAdvertiseData

urlpatterns = [
    url(r'^image/$', images, name='image'),

    url(r'^AllAdvertiseListView/$', AllAdvertiseListView.as_view()),
    url(r'^UserOwnedAdvertiseData/$', UserOwnedAdvertiseData.as_view()),

    url(r'^CreateAdvertiseView/$', CreateAdvertiseView.as_view()),
    url(r'^DeleteAdvertiseData/(?P<pk>[-\w]+)/$', DeleteAdvertiseData.as_view()),
    url(r'^UpdateAdvertiseData/(?P<pk>[-\w]+)/$', UpdateAdvertiseData.as_view()),



]









