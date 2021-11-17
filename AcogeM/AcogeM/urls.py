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
from django.urls import path, include
from AcogeM_app import views

from AcogeM_app.views import CiudadListView, ProtectoraListView, AnimalListView, PerfilListView
from AcogeM_app.views import AnimalDetailView, ProtectoraDetailView,PerfilDetailView
from AcogeM_app.views import AnimalCreateView, AnimalUpdateView, AnimalDeleteView
from AcogeM_app.views import RegistroUsuario

#Django REST API
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index.html'),

    path('ciudades/', CiudadListView.as_view(), name='ciudad-list'),

    path('protectoras/', ProtectoraListView.as_view(), name='protectora-list'),
    path('protectoras/<int:pk>/', ProtectoraDetailView.as_view(), name='protectora-detail'),

    path('animales/', AnimalListView.as_view(), name='animal-list'),
    path('animales/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),

    path('animales/add/', AnimalCreateView.as_view(), name='animal-add'),
    path('animales/<int:pk>/update', AnimalUpdateView.as_view(), name='animal-update'),
    path('animales/<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal-delete'),
    
    path('perfiles/', PerfilListView.as_view(), name='perfil-list'),
    path('perfiles/<int:pk>/', PerfilDetailView.as_view(), name='perfil-detail'),

    #Search
    path('search/', views.search, name='search'),

    #Registrar Usuarios
    path('registrar/', RegistroUsuario, name='user-add'),

	#Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),

    #Django REST API url
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
