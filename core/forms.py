from django import forms
from django.forms import ModelForm
from .models import TipoServicio

class TipoServicioForm(ModelForm):
    class Meta:
        model= TipoServicio
        fields= ['nombreServicio', 'valorServicio', 'descripcionServicio']