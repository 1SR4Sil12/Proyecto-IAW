from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from AcogeM_app.models import Ciudad, Protectora, Animal, Perfil
from django.urls import reverse_lazy

def index(request):
      return render(request,'AcogeM_app/index.html')

# Configurando las vistas

class CiudadListView(ListView):
	model = Ciudad

class ProtectoraListView(ListView):
	model = Protectora

class AnimalListView(ListView):
  	model = Animal

class PerfilListView(ListView):
	model = Perfil

# Configurando las vistas detalle

class AnimalDetailView(DetailView):
	model = Animal

class ProtectoraDetailView(DetailView):
	model = Protectora

class PerfilDetailView(DetailView):
	model = Perfil

# Configurando vistas de edición

class AnimalCreateView(CreateView):
    model = Animal
    fields = ['nom']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = ['nom']

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal-list')



