from __future__ import unicode_literals

from django.db import models

# Create your models here.
class boissons(models.Model):
	name = models.CharField(max_length=60)
	sucre = models.DecimalField(max_digits=5, decimal_places=2)
	description = models.TextField()
	tag = models.ImageField()
	image = models.ImageField()

class Stock(models.Model):
	date_stock = models.DateField()
	product = models.ForeignKey('boissons')
	quantity = models.IntegerField()
