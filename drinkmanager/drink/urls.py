from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^take/(?P<drink_name>\w{2,})$', views.take, name="take"),
    url(r'^show/(?P<drink_name>\w{2,})$', views.show, name="show"),
]
