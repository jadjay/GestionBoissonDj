from django.shortcuts import render
from django.http import HttpResponse
from .models import boissons, Stock

# Create your views here.

def index(request):
    return HttpResponse("Bienvenue en gestion boissons.")

def take(request, boisson_name):
	boisson = get_object_or_404(boissons, pk=name)	
