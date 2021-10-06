from django.contrib import admin

# Register your models here.

from .models import Ciudad, Protectora, Animal, Perfil

admin.site.register(Ciudad)
admin.site.register(Protectora)
admin.site.register(Animal)
admin.site.register(Perfil)