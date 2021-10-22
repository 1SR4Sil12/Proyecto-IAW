from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from AcogeM_app.models import Perfil

# Register your models here.

from .models import Ciudad, Protectora, Animal, Perfil

admin.site.register(Ciudad)
admin.site.register(Protectora)
admin.site.register(Animal)
admin.site.register(Perfil)

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)