from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from AcogeM_app.models import Ciudad, Protectora, Animal, Perfil

class CiudadListView(ListView):
	model = Ciudad

class ProtectoraListView(ListView):
	model = Protectora

# class AnimalListView(ListView):
# 	model = Animal

class PerfilListView(ListView):
	model = Perfil

class AnimalDetailView(DetailView):
	model = Animal

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['Descripcion_animal'] = Animal.objects.all()
	    return context

    # context_object_name = 'animal'
    # queryset = Animal.objects.all()