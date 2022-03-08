from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ciudad(models.Model):
    nom = models.CharField('Nombre', max_length=50)
    pob = models.IntegerField('Población', default=0)
    fotociu = models.ImageField('Imagen', blank=True, null=True, upload_to='img')

    def __str__(self):
    	return f'{self.nom}'

    class Meta:
    	verbose_name_plural = "Ciudades"

class Protectora(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nom = models.CharField('Nombre', max_length=100)
    direc = models.CharField('Direccion', max_length=200)
    fotopro = models.ImageField('Imagen', blank=True, null=True, upload_to='img')

    def __str__(self):
    	return f'{self.nom}: {self.direc}'

    class Meta:
    	verbose_name_plural = "Protectoras"

class Animal(models.Model):

	protectora = models.ForeignKey('Protectora', on_delete=models.CASCADE)
	nom = models.CharField('Nombre', max_length=50)
	descrip = models.TextField('Descripción')
	foto = models.ImageField('Imagen', blank=True, null=True, upload_to='img')

	TIPO_ANIMALES = [
	 	("p", "Perro"),
	 	("g", "Gato"),
	 	("h", "Huron"),
		("c", "Conejo"),
	]

	tipo = models.CharField('Tipo', max_length=1, choices=TIPO_ANIMALES, blank=True, default="p")
	edad = models.IntegerField('Edad', default=0, null=True)
	adoptado = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.nom}'

	class Meta:
		verbose_name_plural = "Animales"

class Perfil(models.Model):
	# nom = models.CharField('Nombre', max_length=30)
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
	ape = models.CharField('Apellidos', max_length=50)
	dni = models.CharField(max_length=9)
	tel = models.IntegerField('Teléfono', blank=True, null=True)
	exp = models.TextField('Experiencia con animales')

	def __str__(self):
		return f'{self.user} {self.ape}'

	class Meta:
		verbose_name_plural = "Perfiles"
			

