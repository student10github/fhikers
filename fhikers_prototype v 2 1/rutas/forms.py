from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ruta, Usuario


# Forms


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Username',
            'first_name': 'Name',
            'last_name': 'Surnames',
            'email': 'Email',
        }


class RutaCreate(forms.ModelForm):

    class Meta:
        model = Ruta
        # fields = '__all__'
        fields = ('foto','titulo','descripcion','distancia','elevacion','tiempo_estimado','nivel_dificultad','numero_de_etapas', 'id_pais', 'id_usuario')


class EtapaForm(forms.ModelForm):

    class Meta:
        model = Etapa

        fields = [
            'titulo_etapa',
            'descripcion_etapa',
            'id_ruta',
        ]




