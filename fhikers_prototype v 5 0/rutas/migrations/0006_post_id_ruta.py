# Generated by Django 3.1.3 on 2020-12-02 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0005_category_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id_ruta',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='rutas.ruta'),
        ),
    ]
