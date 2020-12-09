from django.shortcuts import render, redirect
from django.http import HttpResponse

# Users
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Count Routes
from django.db.models import Count, Q

from .models import Ruta, Etapa, Categoria, Comentario
from .forms import RutaCreate, UserForm, EtapaForm, ComentarioForm


# Contact Form
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Volver a la misma página
from django.urls import reverse



# Create your views here.

# Realiza búsqueda de rutas en la página Home
def home(request):
    busqueda = request.GET.get("buscar")
    shelf = Ruta.objects.all()

    if busqueda:
        shelf = Ruta.objects.filter(
            Q(titulo__icontains=busqueda) |
            Q(numero_de_etapas__icontains=busqueda) |
            Q(tiempo_estimado__icontains=busqueda) |
            Q(distancia__icontains=busqueda) |
            Q(elevacion__icontains=busqueda) |
            Q(nivel_dificultad__icontains=busqueda)
            ).distinct()

    return render(request, 'ruta/home.html', {'shelf': shelf, 'shelf_3': shelf[:3]})


# Carga la página de la ruta
def ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    etapa_id = int(ruta_id)
    comentario_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id=ruta_id)
        etapa_sel = Etapa.objects.filter(id_ruta_id=etapa_id).order_by('numero_etapa')
        comentario_sel = Comentario.objects.filter(id_ruta_id=comentario_id).order_by('fecha_creacion')
    except Ruta.DoesNotExist:
        return redirect('home')
    return render(request, ('ruta/ruta.html', 'ruta/etapa.html', 'ruta/comentario_actualizar.html'), {'ruta_data': ruta_sel, 'etapa_data': etapa_sel, 'comentario_data': comentario_sel})


# CRUD Rutas

# Crea Ruta
def upload_ruta(request):
    upload = RutaCreate()
    if request.method == 'POST':
        upload = RutaCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            # return redirect('home')
            # return redirect('upload_ruta')
            return redirect('welcome')
        else:
            return HttpResponse(""" your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
            return render(request, 'ruta/ruta_crear_y_actualizar.html', {'ruta_form':upload})


# Actualiza Ruta
def update_ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id=ruta_id)
    except Ruta.DoesNotExist:
        return redirect('home')
    ruta_form = RutaCreate(request.POST or None, instance=ruta_sel)
    if ruta_form.is_valid():
       ruta_form.save()
       return redirect('welcome')
    return render(request, 'ruta/ruta_crear_y_actualizar.html', {'ruta_form': ruta_form})

# Borra Ruta
def delete_ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id = ruta_id)
    except Ruta.DoesNotExist:
        return redirect('home')
    ruta_sel.delete()
    return redirect('welcome')


# Sistema de registro de usuarios


# Carga la página inicial del usuario
def welcome(request):
    rutas_usuario = Ruta.objects.filter(id_usuario=request.user.id)
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html", {'rutas_usuario': rutas_usuario})
    # En otro caso redirecionamos al login
    return redirect(request, '/login')


# Registra un nuevo usuario
class UserRegister(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserForm
    success_url = reverse_lazy('login')


# Iniciar sesion de un usuario registrado
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada

                # return redirect('/')
                return redirect('welcome')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


# Finalizar sesion de usuario
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')



# CRUD Stages (Etapa)

# Crea Etapa dentro de una ruta existente
def upload_stage(request):
    upload = EtapaForm()
    if request.method == 'POST':
        upload = EtapaForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('welcome')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{% url 'home' %}">reload</a>""")
    else:
        return render(request, 'ruta/ruta.html', {'etapa_form':upload})


# Actualiza Etapa
def update_stage(request, stage_id):
    stage_id = int(stage_id)
    try:
        stage_sel = Etapa.objects.get(id=stage_id)
    except Etapa.DoesNotExist:
        return redirect('home')
    stage_form = EtapaForm(request.POST or None, instance=stage_sel)
    if stage_form.is_valid():
       stage_form.save()
       return redirect('home')
    return render(request, 'ruta/etapa_actualizar.html', {'etapa_form': stage_form})


# Borra Etapa
def delete_stage(request, stage_id):
    stage_id = int(stage_id)
    try:
        stage_sel = Etapa.objects.get(id = stage_id)
    except Ruta.DoesNotExist:
        return redirect('home')
    stage_sel.delete()
    return redirect('home')


# CRUD Comentarios (BLOG)

# Crea Comentario sobre una ruta
def upload_post(request):
    upload = ComentarioForm()
    if request.method == 'POST':
        upload = ComentarioForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('welcome')
        else:
            return HttpResponse(""" your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
            return render(request, 'ruta/ruta.html', {'upload_post_form':upload})


# Actualiza Comentario
def update_post(request, comentario_id):
    comentario_id = int(comentario_id)
    try:
        comentario_sel = Comentario.objects.get(id=comentario_id)
    except Comentario.DoesNotExist:
        return redirect('home')
    comentario_form = ComentarioForm(request.POST or None, instance=comentario_sel)
    if comentario_form.is_valid():
       comentario_form.save()
       return redirect('welcome')
    return render(request, 'ruta/comentario_actualizar.html', {'upload_form': comentario_form})


# Borra Comentario
def delete_post(request, comentario_id):
    comentario_id = int(comentario_id)
    try:
        comentario_sel = Comentario.objects.get(id = comentario_id)
    except Ruta.DoesNotExist:
        return redirect('home')
    comentario_sel.delete()
    return redirect('welcome')


# Retorna un comentario mediante su id
def one_post(request, idcomentario):
    comentario = Comentario.objects.get(id=idcomentario)
    return render(request, 'ruta/ruta.html', {"post": comentario})

# Retorna una lista de comentarios filtrados por su categoría
def posts_by_category(request, idcategoria):
    categoria = Categoria.objects.get(id=idcategoria)
    comentarios = categoria.comentario_set.order_by("-fecha_creacion")
    return render(request, 'ruta/home.html', {"posts": comentarios})


# Carga la página del blog con todos los comentarios sobre rutas
def blog(request):
    comentarios = Comentario.objects.all()
    return render(request, 'ruta/blog.html', {"posts": comentarios})


# Envia email del mensaje introducido en el formulário de Contacto
def contact_form(request, *args, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    body = render_to_string(
        'ruta/email_contenido.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        },
    )

    email_message = EmailMessage(
        subject='Mensaje de usuario - ' + subject,
        body=body,
        from_email=email,
        to=['emailgithub@gmail.com'],
    )
    email_message.content_subtype = 'html'
    email_message.send()

    return redirect('home')
