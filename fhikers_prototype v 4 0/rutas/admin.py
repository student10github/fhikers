from django.contrib import admin
from .models import Ruta, Usuario, Etapa, Pais, RelacionamentoUsuarioRuta

# Register your models here.

admin.site.register(Ruta)
admin.site.register(Usuario)
admin.site.register(Etapa)
admin.site.register(Pais)
admin.site.register(RelacionamentoUsuarioRuta)