# Generated by Django 3.2.7 on 2022-01-31 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcogeM_app', '0003_auto_20211022_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
    ]
