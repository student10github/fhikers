from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ruta, Usuario, Etapa


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

        labels = {
            'foto': 'Foto',
            'titulo': 'Title',
            'descripcion': 'Description',
            'distancia': 'Distance (KM)',
            'elevacion': 'Elevation (M)',
            'tiempo_estimado': 'Estimated Time (00:00:00)',
            'nivel_dificultad': 'Difficulty',
            'numero_de_etapas': 'Number of Stages',
            'id_pais': 'Pais',
            'id_usuario': 'User',
        }


class EtapaForm(forms.ModelForm):

    class Meta:
        model = Etapa

        fields = [
            'numero_etapa',
            'titulo_etapa',
            'descripcion_etapa',
            'id_ruta',
        ]
        labels = {
            'numero_etapa': 'Stage Number',
            'titulo_etapa': 'Stage Title',
            'descripcion_etapa': 'Stage Description',
            'id_ruta': 'Stage ID',
        }




