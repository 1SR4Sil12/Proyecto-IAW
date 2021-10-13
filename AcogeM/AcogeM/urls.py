"""AcogeM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AcogeM_app.views import CiudadListView, ProtectoraListView, AnimalListView, PerfilListView
from AcogeM_app.views import AnimalDetailView, ProtectoraDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ciudades/', CiudadListView.as_view(), name='ciudad'),
    path('protectoras/', ProtectoraListView.as_view(), name='protectora'),
    path('protectoras/<int:pk>/', ProtectoraDetailView.as_view(), name='protectora-detail'),
    path('animales/', AnimalListView.as_view(), name='animal'),
    path('animales/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('perfiles/', PerfilListView.as_view(), name='perfil'),
]
