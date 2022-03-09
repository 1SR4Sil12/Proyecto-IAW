from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from AcogeM_app.models import Ciudad, Protectora, Animal, Perfil, User
from AcogeM_app.forms import AnimalForm, PerfilForm, AdoptadoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.http import HttpResponseRedirect

def index(request):
      return render(request,'AcogeM_app/index.html')

# ------------------- Configurando las vistas -------------------
class CiudadListView(ListView):
	model = Ciudad
	template_name = 'AcogeM_app/ciudad_list'
	paginate_by = 3

class ProtectoraListView(ListView):
	model = Protectora
	template_name = 'AcogeM_app/protectora_list.html'
	paginate_by = 3

class AnimalListView(ListView):
  	model = Animal
  	template_name = 'AcogeM_app/animal_list.html'
  	paginate_by = 3

class PerfilListView(LoginRequiredMixin, ListView):
	model = Perfil

# ---------------- Configurando las vistas detalle --------------
class AnimalDetailView(DetailView):
	model = Animal


def adopcion(request):
	if request.method == "POST":
		for i in Animal.objects.raw('SELECT id from AcogeM_app_animal'):
			print(i)
			# for i in Animal.objects.raw('UPDATE AcogeM_app_animal set adoptado = True where id = %'):
			# 	print(p.adoptado)
		return render(request, 'AcogeM_app/adoptado.html')
	

class ProtectoraDetailView(DetailView):
	model = Protectora

class PerfilDetailView(DetailView):
	model = Perfil


# --------------- Vistas Creación, Detalle y Borrado --------------
class AnimalCreateView(LoginRequiredMixin, CreateView):
	model = Animal
	form_class = AnimalForm
	success_url = reverse_lazy('animal-list')

class AnimalUpdateView(LoginRequiredMixin, UpdateView):
	model = Animal
	form_class = AnimalForm
	success_url = reverse_lazy('animal-list')

class AnimalAdoptadoView(LoginRequiredMixin, UpdateView):
	model = Animal
	form_class = AdoptadoForm
	success_url = reverse_lazy('animal-list')

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy('animal-list')


# --------------- Registro de Usuario ------------------------------
def RegistroUsuario(request):
	if request.method == "POST":
		UForm = UserCreationForm(request.POST)
		PForm = PerfilForm(request.POST)
		if UForm.is_valid() and PForm.is_valid():
			Usuario = UForm.save(commit=False)
			Perfil = PForm.save(commit=False)
			Perfil.user = Usuario
			UForm.save()
			PForm.save()
			username = UForm.cleaned_data['username']
			password = UForm.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index.html')
	else:
		UForm = UserCreationForm
		PForm = PerfilForm

	return render(request, 'registration/registro.html', {'UForm': UForm, 'PForm': PForm})


# --------------- Barra de búsqueda ---------------------------------
def search(request):
	if request.method == "POST":
		buscar = request.POST['buscar']
		animales = Animal.objects.filter(nom__contains=buscar)
		ciudades = Ciudad.objects.filter(nom__contains=buscar)
		protectoras = Protectora.objects.filter(nom__contains=buscar)

		return render(request, 
			'AcogeM_app/search.html',
			{'buscar':buscar,
			'animales':animales,
			'ciudades':ciudades,
			'protectoras':protectoras})
	else:
		return render(request, 
			'AcogeM_app/search.html',
			{})


# ---------------- Actualizar Usuario -----------------
class PerfilUpdateView(LoginRequiredMixin, UpdateView):
	model = Perfil
	form_class = PerfilForm
	success_url = reverse_lazy('index.html')

#--------------- Politica de Privacidad ---------------
class politica(TemplateView):
	template_name = 'AcogeM_app/politica.html'







