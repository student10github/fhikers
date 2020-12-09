from django.contrib import admin
from .models import Ruta, Usuario, Etapa, Pais, RelacionamentoUsuarioRuta, Post, Category

# Register your models here.

admin.site.register(Ruta)
admin.site.register(Usuario)
admin.site.register(Etapa)
admin.site.register(Pais)
admin.site.register(RelacionamentoUsuarioRuta)
admin.site.register(Post)
admin.site.register(Category)