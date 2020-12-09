# Generated by Django 3.1.1 on 2020-11-30 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rutas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='id_etapa',
        ),
        migrations.AddField(
            model_name='etapa',
            name='id_ruta',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rutas.ruta'),
        ),
        migrations.AddField(
            model_name='pais',
            name='codigo_pais',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='id_pais',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rutas.pais'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='id_usuario',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
