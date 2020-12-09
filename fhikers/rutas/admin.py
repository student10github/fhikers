from django.contrib import admin
from .models import Ruta, Etapa, Pais, Comentario, Categoria

# Register your models here.

admin.site.register(Ruta)
admin.site.register(Etapa)
admin.site.register(Pais)
admin.site.register(Comentario)
admin.site.register(Categoria)