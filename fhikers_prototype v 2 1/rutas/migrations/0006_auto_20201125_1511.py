# Generated by Django 3.1.3 on 2020-11-25 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0005_auto_20201125_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='id_etapa',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rutas.etapa'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='id_pais',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rutas.pais'),
        ),
        migrations.AddField(
            model_name='ruta',
            name='id_usuario',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rutas.usuario'),
        ),
    ]
