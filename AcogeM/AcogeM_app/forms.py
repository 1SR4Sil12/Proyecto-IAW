from django import forms
from AcogeM_app.models import Animal

# class AnimalForm(forms.Form):
# 	nom = forms.CharField(required=True)
# 	descrip = forms.CharField(required=True)
# 	tipo = forms.CharField(required=True)

class AnimalForm(forms.ModelForm):
	class Meta:
		model = Animal
		exclude = ['created_at', 'created_by', 'last_modified_by']