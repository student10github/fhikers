# Generated by Django 3.1.1 on 2020-11-25 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0004_remove_ruta_id_etapa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='id_pais',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='id_usuario',
        ),
    ]
