from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from AcogeM_app.models import Ciudad, Protectora, Animal, Perfil, User
from AcogeM_app.forms import AnimalForm, PerfilForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q

def index(request):
      return render(request,'AcogeM_app/index.html')

# Configurando las vistas

class CiudadListView(ListView):
	model = Ciudad

class ProtectoraListView(ListView):
	model = Protectora

class AnimalListView(ListView):
  	model = Animal

class PerfilListView(LoginRequiredMixin, ListView):
	model = Perfil

# Configurando las vistas detalle

class AnimalDetailView(DetailView):
	model = Animal

class ProtectoraDetailView(DetailView):
	model = Protectora

class PerfilDetailView(DetailView):
	model = Perfil

# Configurando vistas de edición

# Estas son las primeras formas en las que creé las vistas, la primera va enlazada
# con el forms.py de tal forma que en dicho archivo le digo los campos que quiero que forme
# parte del formulario. La segunda ya es, con todos los campos excluyendo unos cuantos. En la
# vista lo que tengo que hacer es especificar los campos que quiero completar.

# def animal_create(request, pk):
# 	animal = get_object_or_404(Animal, pk=pk)
# 	if request.method == 'POST':
# 		form = AnimalForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = AnimalForm(instance=animal)
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'AcogeM_app/animal_form.html', context)

# def animal_edit(request, pk):
# 	animal = get_object_or_404(Animal, pk=pk)
# 	if request.method == 'POST':
# 		form = AnimalForm(request.POST, instance=animal)
# 		if form.is_valid():
# 			# animal.nom = form.cleaned_data['nom']
# 			# animal.descrip = form.cleaned_data['descrip']
# 			# animal.tipo = form.cleaned_data['tipo']
# 			# animal.save()
# 			form.save()
# 	else:
# 		# form = AnimalForm(initial={
# 		# 	'nom': animal.nom,
# 		# 	'descrip': animal.descrip,
# 		# 	'tipo': animal.tipo,
# 		# 	})
# 		form = AnimalForm(instance=animal)
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'AcogeM_app/animal_form.html', context)
# 	success_url = reverse_lazy('animal-list')

class AnimalCreateView(LoginRequiredMixin, CreateView):
	model = Animal
	form_class = AnimalForm
	success_url = reverse_lazy('animal-list')

class AnimalUpdateView(LoginRequiredMixin, UpdateView):
	model = Animal
	form_class = AnimalForm
	success_url = reverse_lazy('animal-list')

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy('animal-list')

# --------------- Registro de Usuario -----------------
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

# --------------- Barra de búsqueda -------------------
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





