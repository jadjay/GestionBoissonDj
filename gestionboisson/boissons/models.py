from __future__ import unicode_literals

from django.db import models

# Create your models here.
class boissons(models.Model):
	def __str__(self):
		return "%s" % (self.name)
	name = models.CharField(max_length=60)
	sucre = models.DecimalField(max_digits=5, decimal_places=2)
	description = models.TextField()
	tag = models.ImageField()
	image = models.ImageField()

class Stock(models.Model):
	def __str__(self):
		return "%s-%s %s units" % (self.date_stock.strftime("%F"),self.product.name,self.quantity)
	date_stock = models.DateField()
	product = models.ForeignKey('boissons')
	quantity = models.IntegerField()
