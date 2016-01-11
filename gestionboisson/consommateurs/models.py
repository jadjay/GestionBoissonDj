from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from boissons.models import boissons

# Create your models here.
class consommateurs(models.Model):
	def __str__(self):
		return "%s" % (self.user.username)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	activation_key = models.CharField(max_length=60)
	key_expires = models.DateTimeField()

class consommation(models.Model):
	def __str__(self):
		manuel = "MANUEL" if self.manuel else ""
		return "%s %s %s %s" % (self.date.strftime("%F"),self.consommateur.user.username,self.boisson.name,manuel)
	date = models.DateField(auto_now_add=True)
	consommateur = models.ForeignKey('consommateurs')
	boisson = models.ForeignKey('boissons.boissons')
	manuel = models.BooleanField(default=True)

class ConsommateursForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
