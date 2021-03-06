from django.urls import path
from . import views
from fhikers_proj.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('ruta/<int:ruta_id>', views.ruta, name='ruta'),
    path('upload/', views.upload, name = 'upload-ruta'),
    path('update/<int:ruta_id>', views.update_ruta),
    path('delete/<int:ruta_id>', views.delete_ruta),

    # Stage
    path('upload_stage/', views.upload_stage, name='upload_stage'),
    path('ruta/update_stage/<int:stage_id>', views.update_stage, name='update_stage'),
    path('ruta/delete_stage/<int:stage_id>', views.delete_stage, name='delete_stage'),
]

#DataFlair

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)