from django.shortcuts import render, redirect
from .models import Ruta
from .forms import RutaCreate
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = Ruta.objects.all()
    return render(request, 'ruta/rutas.html', {'shelf': shelf})

def upload(request):
    upload = RutaCreate()
    if request.method == 'POST':
        upload = RutaCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
            return render(request, 'ruta/upload_form.html', {'upload_form':upload})


def update_ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id = ruta_id)
    except Ruta.DoesNotExist:
        return redirect('index')
    ruta_form = RutaCreate(request.POST or None, instance = ruta_sel)
    if ruta_form.is_valid():
       ruta_form.save()
       return redirect('index')
    return render(request, 'ruta/upload_form.html', {'upload_form':ruta_form})


def delete_ruta(request, ruta_id):
    ruta_id = int(ruta_id)
    try:
        ruta_sel = Ruta.objects.get(id = ruta_id)
    except Ruta.DoesNotExist:
        return redirect('index')
    ruta_sel.delete()
    return redirect('index')