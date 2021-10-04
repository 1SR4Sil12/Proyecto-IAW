from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField('Nombre', max_length=50)

class Protectora(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=100)
    direccion = models.CharField('Direccion', max_length=200)

class Animal(models.Model):
	protectora = models.ForeignKey(Protectora, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=50)
	nombre = models.CharField('Nombre', max_length=50)
	descripcion = models.CharField('Descripción', max_length=200)
	foto = models.ImageField('Imagen', blank=True, null=True, upload_to=localizacion_imagen)

