from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Servicio, Perfil

class ServicioForm(ModelForm):

    nombre_servicio = forms.CharField(min_length=4, max_length=100)
    valor_servicio  = forms.IntegerField(min_value=1)
    nombre_servicio = forms.CharField(min_length=4, max_length=250)

    class Meta:
        model= Servicio
        fields= ['nombre_servicio', 'valor_servicio', 'descripcion_servicio', 'fecha_servicio']
        #exclude = ('cliente',)
        labels={
            'fecha_servicio':'Fecha de servicio'
        }

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['direccion','comuna', 'ciudad', 'tipo_domicilio', 'servicio']
        exclude = ('servicio',)
        labels={
            'tipo_domicilio':'Tipo de domicilio'
        }
        
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1','password2']
        labels={
            'email':'Email'
        }