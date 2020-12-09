from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your models here.

class Pais(models.Model):
    codigo_pais = models.CharField(max_length=2, blank=False, default='')
    nombre_pais = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        cadena = self.codigo_pais + " - " + self.nombre_pais
        return cadena


class Ruta(models.Model):
    LEVEL_CHOICES = (
        ('EASY', 'easy'),
        ('MODERATE', 'moderate'),
        ('HIGH', 'high'),
        ('CHALLENGING', 'challenging'),
    )
    foto = models.ImageField()
    titulo = models.CharField(max_length=100, blank=False, default='')
    descripcion = models.CharField(max_length=255, blank=False, default='')
    distancia = models.IntegerField()
    elevacion = models.IntegerField()
    tiempo_estimado = models.DurationField()
    nivel_dificultad = models.CharField(max_length=11, choices=LEVEL_CHOICES, default='EASY')
    numero_de_etapas = models.IntegerField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default='', blank=True, null=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.titulo


class Etapa(models.Model):
    numero_etapa = models.IntegerField(blank=False, default=0)
    titulo_etapa = models.CharField(max_length=100, blank=False, default='')
    descripcion_etapa = models.CharField(max_length=255, blank=False, default='')
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.titulo_etapa


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='', blank=True, null=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, default='', blank=True, null=True)
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.titulo