from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^take/(?P<boisson_name>[-:\w]+)', views.take, name='take'),
]
