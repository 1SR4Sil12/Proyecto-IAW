# Generated by Django 3.2.7 on 2021-10-06 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre')),
                ('pob', models.IntegerField(default=0, verbose_name='Población')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nombre')),
                ('ape', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=9)),
                ('tel', models.IntegerField(blank=True, null=True, verbose_name='Teléfono')),
                ('exp', models.CharField(max_length=200, verbose_name='Experiencia con animales')),
            ],
        ),
        migrations.CreateModel(
            name='Protectora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direc', models.CharField(max_length=200, verbose_name='Direccion')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcogeM_app.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descrip', models.CharField(max_length=200, verbose_name='Descripción')),
                ('tipo', models.CharField(blank=True, choices=[('p', 'Perro'), ('g', 'Gato'), ('h', 'Huron'), ('c', 'Conejo')], default='p', max_length=1, verbose_name='Tipo')),
                ('protectora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AcogeM_app.protectora')),
            ],
        ),
    ]