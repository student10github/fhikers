from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.contrib.sessions.models import Session

# Create your models here.

"""
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False, default='')
    primer_apellido = models.CharField(max_length=50, blank=False, default='')
    segundo_apellido = models.CharField(max_length=50, blank=False, default='')
    sexo = models.CharField(max_length=10, blank=False, default='')
    fecha_nacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre
"""

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('You have to put an email')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            password=password
        )
        user.usuario_administrador=True
        user.save()
        return user



class Usuario(AbstractBaseUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (OTHERS, 'others'),
    )
    username = models.CharField('Username', unique=True, max_length=100)
    email = models.EmailField('Email', max_length=254, unique=True)
    nombre = models.CharField('Name', max_length=200, blank=True, null=True)
    primer_apellido = models.CharField('Primer Apellido', max_length=200, blank=True, null=True)
    segundo_apellido = models.CharField('Segundo Apellido', max_length=200, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES, default=FEMALE)
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField('Perfil Image', upload_to='media/', height_field=None, width_field=None, max_length=200)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombre},{self.segundo_apellido}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
























class Etapa(models.Model):
    titulo_etapa = models.CharField(max_length=100, blank=False, default='')
    descripcion_etapa = models.CharField(max_length=255, blank=False, default='')
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.titulo_etapa)


class Pais(models.Model):
    codigo_pais = models.CharField(max_length=2, blank=False, default='')
    nombre_pais = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        cadena = self.codigo_pais + " - " + self.nombre_pais
        return cadena


class Ruta(models.Model):
    foto = models.ImageField()
    titulo = models.CharField(max_length=100, blank=False, default='')
    descripcion = models.CharField(max_length=255, blank=False, default='')
    distancia = models.CharField(max_length=10, blank=False, default='')
    elevacion = models.CharField(max_length=10, blank=False, default='')
    tiempo_estimado = models.DurationField()
    nivel_dificultad = models.CharField(max_length=10, blank=False, default='')
    numero_de_etapas = models.IntegerField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='', blank=True, null=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.titulo


class RelacionamentoUsuarioRuta(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    interesado = models.CharField(max_length=50, blank=False, default='')
    recomienda = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.id_usuario


