from django.contrib import admin

# Register your models here.
from .models import consommateurs, consommation

admin.site.register(consommateurs)
admin.site.register(consommation)

