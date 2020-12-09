# Generated by Django 3.1.3 on 2020-11-24 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_etapa', models.CharField(default='', max_length=100)),
                ('descripcion_etapa', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('primer_apellido', models.CharField(default='', max_length=50)),
                ('segundo_apellido', models.CharField(default='', max_length=50)),
                ('sexo', models.CharField(default='', max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='img/')),
                ('titulo', models.CharField(default='', max_length=100)),
                ('descripcion', models.CharField(default='', max_length=255)),
                ('distancia', models.CharField(default='', max_length=10)),
                ('elevacion', models.CharField(default='', max_length=10)),
                ('tiempo_estimado', models.DurationField()),
                ('nivel_dificultad', models.CharField(default='', max_length=10)),
                ('numero_de_etapas', models.IntegerField()),
                ('id_etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutas.etapa')),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutas.pais')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='RelacionamentoUsuarioRuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interesado', models.CharField(default='', max_length=50)),
                ('recomienda', models.CharField(default='', max_length=50)),
                ('id_ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutas.ruta')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutas.usuario')),
            ],
        ),
    ]