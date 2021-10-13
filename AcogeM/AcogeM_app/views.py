from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from AcogeM_app.models import Ciudad, Protectora, Animal, Perfil

class CiudadListView(ListView):
	model = Ciudad

class ProtectoraListView(ListView):
	model = Protectora

class AnimalListView(ListView):
  	model = Animal

class PerfilListView(ListView):
	model = Perfil

class AnimalDetailView(DetailView):
	model = Animal

class ProtectoraDetailView(DetailView):
	model = Protectora