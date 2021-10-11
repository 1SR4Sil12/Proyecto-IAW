from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from AcogeM_app.models import Ciudad

class CiudadListView(ListView):
	model = Ciudad