from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from AcogeM_app.models import Ciudad, Protectora, Animal, Perfil
from AcogeM_app.forms import AnimalForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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



