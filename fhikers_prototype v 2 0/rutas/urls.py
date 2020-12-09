from django.urls import path
from . import views
from fhikers_proj.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-ruta'),
    path('update/<int:ruta_id>', views.update_ruta),
    path('delete/<int:ruta_id>', views.delete_ruta)
]

#DataFlair

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)