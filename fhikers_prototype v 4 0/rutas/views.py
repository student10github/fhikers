from django.shortcuts import render, redirect
from .models import Ruta, Usuario, Etapa
from .forms import RutaCreate, UserForm, EtapaForm
from django.http import HttpResponse

# Users imports
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Cuenta las rutas
from django.db.models import Count, Q


# Create your views here.

def index(request):
    busqueda = request.GET.get("buscar")
    shelf = Ruta.objects.all()

    if busqueda:
        shelf = Ruta.objects.filter(
            Q(titulo__icontains=busqueda) |
            # Q(id_pais__icontains=busqueda) |
            Q(numero_de_etapas__icontains=busqueda) |
            Q(tiempo_estimado__icontains=busqueda) |
            Q(distancia__icontains=busqueda) |
            Q(elevacion__icontains=busqueda) |
            Q(nivel_dificultad__icontains=busqueda)
            ).distinct()

    return render(request, 'ruta/rutas.html', {'shelf': shelf, 'shelf_3': shelf[:3]})


def ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    etapa_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id=ruta_id)
        etapa_sel = Etapa.objects.filter(id_ruta_id=etapa_id).order_by('numero_etapa')
        # etapa_sel = Etapa.objects.filter(id_ruta_id=etapa_id).order_by('numero_etapa')
    except Ruta.DoesNotExist:
        return redirect('index')
    return render(request, ('ruta/ruta.html', 'ruta/etapa.html'), {'ruta_data': ruta_sel, 'etapa_data': etapa_sel})


# CRUD Rutas


def upload(request):
    upload = RutaCreate()
    if request.method == 'POST':
        upload = RutaCreate(request.POST, request.FILES)
        if upload.is_valid():
            # upload.Meta.fields.id_usuario = request.POST.request.user.id
            # Ruta.objects.get(id_usuario=request.user.id)      , {'id_usuario_id':request.user.id}

            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
            return render(request, 'ruta/upload_form.html', {'upload_form':upload})


def update_ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id=ruta_id)
    except Ruta.DoesNotExist:
        return redirect('index')
    ruta_form = RutaCreate(request.POST or None, instance=ruta_sel)
    if ruta_form.is_valid():
       ruta_form.save()
       return redirect('index')
    return render(request, 'ruta/upload_form.html', {'upload_form': ruta_form})


def delete_ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id = ruta_id)
    except Ruta.DoesNotExist:
        return redirect('index')
    ruta_sel.delete()
    return redirect('index')


# Sistema de registro de usuarios

def welcome(request):
    shelf = Ruta.objects.filter(id_usuario=request.user.id)
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        # return render(request, "welcome.html", {'shelf': shelf, 'total': total})
        return render(request, "welcome.html", {'shelf': shelf})
    # En otro caso redirecionamos al login
    return redirect(request, '/login')


# Clase utilizada en lugar de la funcion register
class UserRegister(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserForm
    success_url = reverse_lazy('login')


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


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')



# CRUD Stages


def upload_stage(request):
    upload = EtapaForm()
    if request.method == 'POST':
        upload = EtapaForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
            return render(request, 'ruta/ruta.html', {'upload_stage_form':upload})


def update_stage(request, stage_id):
    stage_id = int(stage_id)
    try:
        stage_sel = Etapa.objects.get(id=stage_id)
    except Etapa.DoesNotExist:
        return redirect('index')
    stage_form = EtapaForm(request.POST or None, instance=stage_sel)
    if stage_form.is_valid():
       stage_form.save()
       return redirect('index')
    return render(request, 'ruta/update_etapa.html', {'upload_form': stage_form})


def delete_stage(request, stage_id):
    stage_id = int(stage_id)
    try:
        stage_sel = Etapa.objects.get(id = stage_id)
    except Ruta.DoesNotExist:
        return redirect('index')
    stage_sel.delete()
    return redirect('index')


