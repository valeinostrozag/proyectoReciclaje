from django.shortcuts import render, redirect 
from .models import TipoServicio
from .forms import TipoServicioForm

# Create your views here.
def home (request):

    return render(request, 'core/home.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

def mantenedor(request):
    servicios= TipoServicio.objects.all()
    data = {
        'servicios': servicios
    }
    return render(request, 'core/mantenedor.html', data)

def agregarServicio(request):
    data = {
        'form': TipoServicioForm()
    }

    if request.method == "POST":
        formulario = TipoServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Guardado Correctamente"
   
    return render(request, 'core/agregarServicio.html', data)

def modificarServicio(request, id):
    tipoServicio = TipoServicio.objects.get(id=id)
    data = {
        'form': TipoServicioForm(instance=tipoServicio)
    }
    if request.method == "POST":
        formulario = TipoServicioForm(data=request.POST, instance=tipoServicio)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    
    return render(request, 'core/modificarServicio.html', data)

def eliminarServicio(request, id):
    tipoServicio = TipoServicio.objects.get(id=id)
    tipoServicio.delete()

    return redirect(to="mantenedor")
