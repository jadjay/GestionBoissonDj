from django.contrib import admin

# Register your models here.
from .models import boissons, Stock

admin.site.register(boissons)
admin.site.register(Stock)

