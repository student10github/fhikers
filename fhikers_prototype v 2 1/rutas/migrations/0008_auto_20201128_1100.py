# Generated by Django 3.1.1 on 2020-11-28 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rutas', '0007_auto_20201126_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacionamentousuarioruta',
            name='id_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
