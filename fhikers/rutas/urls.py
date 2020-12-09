from django.urls import path
from . import views
from fhikers_proj.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

# from django.conf.urls import patterns, include, url
from django.conf.urls import include, url

urlpatterns = [

    path('', views.home, name = 'home'),

    # Rutas (Routes) - CRUD
    path('upload_ruta/', views.upload_ruta, name = 'upload_ruta'),
    path('ruta/<int:ruta_id>', views.ruta, name='ruta'),
    path('update/<int:ruta_id>', views.update_ruta),
    path('delete/<int:ruta_id>', views.delete_ruta),

    # Etapas (Stage) - CUD
    path('upload_stage/', views.upload_stage, name='upload_stage'),
    path('ruta/update_stage/<int:stage_id>', views.update_stage, name='update_stage'),
    path('ruta/delete_stage/<int:stage_id>', views.delete_stage, name='delete_stage'),

    # Blog (Posts) - CRUD
    path('upload_post/', views.upload_post, name='upload_post'),
    path('post/<int:id>', views.one_post, name="one_post"),
    path('category/<int:id>', views.posts_by_category, name="posts_by_category"),
    path('ruta/update_post/<int:comentario_id>', views.update_post, name='update_post'),
    path('ruta/delete_post/<int:comentario_id>', views.delete_post, name='delete_post'),

    path('blog/', views.blog, name='blog'),
    path('blog/update_post/<int:comentario_id>', views.update_post, name='update_post'),
    path('blog/delete_post/<int:comentario_id>', views.delete_post, name='delete_post'),

    # Contact Form
    path('contact_form/', views.contact_form, name='contact_form'),

]

# Data Flair

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)