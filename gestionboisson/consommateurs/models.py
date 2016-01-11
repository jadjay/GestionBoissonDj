from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from boissons.models import boissons

# Create your models here.
class consommateurs(models.Model):
	def __str__(self):
		return "%s" % (self.user.username)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class consommation(models.Model):
	def __str__(self):
		manuel = "MANUEL" if self.manuel else ""
		return "%s %s %s %s" % (self.date.strftime("%F"),self.consommateur.user.username,self.boisson.name,manuel)
	date = models.DateField(auto_now_add=True)
	consommateur = models.ForeignKey('consommateurs')
	boisson = models.ForeignKey('boissons.boissons')
	manuel = models.BooleanField(default=True)
