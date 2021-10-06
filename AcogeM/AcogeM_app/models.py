from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nom = models.CharField('Nombre', max_length=50)
    pob = models.IntegerField('Población', default=0)

class Protectora(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nom = models.CharField('Nombre', max_length=100)
    direc = models.CharField('Direccion', max_length=200)

class Animal(models.Model):

	LOAN_STATUS (
		("p", "Perro"),
		("g", "Gato"),
		("h", "Huron"),
		("c", "Conejo"),
	)

	tipo = models.CharField('Tipo', max_length=1, choices=LOAN_STATUS, default="p")
	protectora = models.ForeignKey('Protectora', on_delete=models.CASCADE)
	nom = models.CharField('Nombre', max_length=50)
	descrip = models.CharField('Descripción', max_length=200)
#	foto = models.ImageField('Imagen', blank=True, null=True, upload_to=localizacion_imagen)

class User(models.Model):
	nom = models.CharField('Nombre', max_length=30)
	ape = models.CharField('Apellidos', max_length=50)
	dni = forms.ESIdentityCardNumberField(only_nif=True)
	tel = models.IntegerField('Teléfono', max_digits=9)
	exp = models.CharField('Experiencia con animales', max_length=200)

