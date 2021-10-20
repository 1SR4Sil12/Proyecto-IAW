from django.core.management.base import BaseCommand, CommandError
from AcogeM_app.models import Ciudad

class Command(BaseCommand):
	help = 'Crear un nuevo registro de Ciudad'

	def add_arguments(self, parser):
		parser.add_argument('nom', help="Especifica el nombre de la Ciudad")
		parser.add_argument('-p', '--poblacion', help="Especifica el número de habitantes")

	def handle(self, *args, **options):
		name = options['nom']
		poblacion = options['poblacion']

		Ciudad.objects.create(nom=name, pob=poblacion)
		self.stdout.write('Ciudad creada con éxito')