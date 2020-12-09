from django.db import models

# Create your models here.

class Etapa(models.Model):
    titulo_etapa = models.CharField(max_length=100, blank=False, default='')
    descripcion_etapa = models.CharField(max_length=255, blank=False, default='')

    def __str__(self):
        return self.titulo_etapa

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.nombre_pais

# CREAR APP PARA ESTE
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False, default='')
    primer_apellido = models.CharField(max_length=50, blank=False, default='')
    segundo_apellido = models.CharField(max_length=50, blank=False, default='')
    sexo = models.CharField(max_length=10, blank=False, default='')
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    foto = models.ImageField()
    titulo = models.CharField(max_length=100, blank=False, default='')
    descripcion = models.CharField(max_length=255, blank=False, default='')
    distancia = models.CharField(max_length=10, blank=False, default='')
    elevacion = models.CharField(max_length=10, blank=False, default='')
    tiempo_estimado = models.DurationField()
    nivel_dificultad = models.CharField(max_length=10, blank=False, default='')
    numero_de_etapas = models.IntegerField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class RelacionamentoUsuarioRuta(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    interesado = models.CharField(max_length=50, blank=False, default='')
    recomienda = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.id_usuario