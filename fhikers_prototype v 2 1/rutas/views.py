from django.shortcuts import render, redirect
from .models import Ruta, Usuario
from .forms import RutaCreate, UserForm
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
from django.db.models import Count


# Create your views here.

def index(request):
    shelf = Ruta.objects.all()
    return render(request, 'ruta/rutas.html', {'shelf': shelf, 'shelf_3': shelf[:3]})


def ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id=ruta_id)
    except Ruta.DoesNotExist:
        return redirect('index')
    return render(request, 'ruta/ruta.html', {'ruta_data': ruta_sel})


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


# SISTEMA DE REGISTROS

def welcome(request):
    shelf = Ruta.objects.filter(id_usuario=request.user.id)
    # total = Ruta.objects.aggregate(Count('id'))     #Resultado es  {'id__count': 6}
    total = Ruta.objects.annotate(Count('id'))      # Resultado es  <QuerySet [<Ruta: Titulo admin3>, <Ruta: dentro del admin2 elegir admin7>, <Ruta: Titulo admin2>, <Ruta: Carros de Foc>, <Ruta: PEAKS OF EUROPE>, <Ruta: CAMI DE CAVALLS (MENORCA)>]>
    total = total[0].id__count

    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html", {'shelf': shelf, 'total': total})
    # En otro caso redirecionamos al login
    return redirect(request, '/login')


# Clase utilizada en lugar de la funcion register
class UserRegister(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserForm
    success_url = reverse_lazy('welcome')


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
