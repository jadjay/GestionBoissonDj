from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from boissons.models import boissons

# Create your models here.
class consommateurs(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
#	mail = models.EmailField()
#	date = models.DateField(auto_now_add=True)
#	lastdate = models.DateField(auto_now=True)
#	password = models.CharField(max_length=600)

class consommation(models.Model):
	date = models.DateField(auto_now_add=True)
	consommateur = models.ForeignKey('consommateurs')
	boisson = models.ForeignKey('boissons.boissons')
