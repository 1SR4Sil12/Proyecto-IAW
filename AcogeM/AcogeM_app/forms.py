from django import forms
from AcogeM_app.models import Animal

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