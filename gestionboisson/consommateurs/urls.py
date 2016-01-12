from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new', views.new, name='new'),
	url(r'^register', views.register, name='register'),
	url(r'^confirm', views.confirm, name='confirm'),
	url(r'^accounts/', include('registration.backends.hmac.urls')),
]
