# Generated by Django 3.2.7 on 2021-10-22 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AcogeM_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]