from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from gestionboissons.boissons.models import boissons

# Create your models here.
class users(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mail = models.EmailField()
	date = DateField(auto_now_add=True)
	lastdate = DateField(auto_now=True)
	password = models.CharField(max_length=600)

class consommation(models.Model):
	date = DateField(auto_now_add=True)
	user = models.ForeignKey('users')
	boisson = models.ForeignKey('boissons.boissons')
