from django import forms
from .models import Ruta

#DataFlair

class RutaCreate(forms.ModelForm):
    class Meta:
        model = Ruta
        # fields = '__all__'
        fields = ('foto','titulo','descripcion','distancia','elevacion','tiempo_estimado','nivel_dificultad','numero_de_etapas')
