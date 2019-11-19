from django.shortcuts import render, redirect 
from .models import Servicio, Perfil
from .forms import ServicioForm, CustomUserForm, PerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate

# Create your views here.
def home (request):

    return render(request, 'core/home.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

@login_required
def mantenedor(request):
    servicios= Servicio.objects.all()
    data = {
        'servicios': servicios
    }
    return render(request, 'core/mantenedor.html', data)

@login_required
def agregar_servicio(request):
    data = {
        'form': ServicioForm()
    }

    if request.method == "POST":
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Guardado Correctamente"
   
    return render(request, 'core/agregarServicio.html', data)

@login_required
def modificar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    data = {
        'form': ServicioForm(instance=servicio)
    }
    if request.method == "POST":
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    
    return render(request, 'core/modificarServicio.html', data)

@login_required
def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()

    return redirect(to="mantenedor")

def registrar_usuario(request):

    data = {
        'form': CustomUserForm(),
        'perfil': PerfilForm()
    }

    if request.method=='POST':

        formulario = CustomUserForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if formulario.is_valid() and perfil_form.is_valid():

            usuario_nuevo = formulario.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = usuario_nuevo
            perfil.save()
            
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            #logueamos el usuario
            auth_login(request, user)

            return redirect(to='home')
            
        data['form']=formulario
        data['perfil']=perfil_form

    return render(request, 'registration/registrar.html', data)

@login_required
def contratar_servicio(request, id):
    user = request.user
    servicio = Servicio.objects.get(id=id)

    servicio.cliente = user
    servicio.save()

    return redirect(to='perfil')

@login_required
def perfil(request):

    user = request.user
    perfil = Perfil.objects.get(user_id = user.id)
    #servicio = Servicio.objects.get(cliente_id=user.id)
    data={      
        'perfil': perfil
        #'servicio': servicio
    }
    return render(request, 'core/perfil.html', data)