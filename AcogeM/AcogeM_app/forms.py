from django import forms
from AcogeM_app.models import Animal, Perfil

# Una forma de crear el formulario, especificandole los campos que quiero, de la
# forma uso todos los campos, y excluyo algunos.

# class AnimalForm(forms.Form):
# 	nom = forms.CharField(required=True)
# 	descrip = forms.CharField(required=True)
# 	tipo = forms.CharField(required=True)

class AnimalForm(forms.ModelForm):
	class Meta:
		model = Animal
		exclude = ['created_at', 'created_by', 'last_modified_by']

# class UserForm(forms.ModelForm):
# 	username = forms.CharField(max_length=30)
# 	password = forms.CharField(max_length=20, widget=forms.PasswordInput)
# 	email = forms.CharField(max_length=50)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'password', 'email')
# 		# exclude = ['created_at', 'created_by', 'last_modified_by', 'last_login', 'groups', 'user_permissions', 'date_joined']

class PerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('ape', 'dni', 'tel', 'exp')