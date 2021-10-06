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

	PERRO = 1
	GATO = 2
	HURON = 3
	CONEJO = 4

	TIPOS_ANIMALES (
		(PERRO, "Perro"),
		(GATO, "Gato"),
		(HURON, "Huron"),
		(CONEJO, "Conejo"),
	)

	protectora = models.ForeignKey(Protectora, on_delete=models.CASCADE)
	tipo = models.PositiveSmallIntegerField('Tipo', choices=TIPOS_ANIMALES, default=PERRO)
	nom = models.CharField('Nombre', max_length=50)
	descrip = models.CharField('Descripción', max_length=200)
#	foto = models.ImageField('Imagen', blank=True, null=True, upload_to=localizacion_imagen)

class User(models.Model):
	nom = models.CharField('Nombre', max_length=30)
	ape = models.CharField('Apellidos', max_length=50)
	dni = forms.ESIdentityCardNumberField(only_nif=True)
	tel = models.IntegerField('Teléfono', max_digits=9)
	exp = models.CharField('Experiencia con animales', max_length=200)

