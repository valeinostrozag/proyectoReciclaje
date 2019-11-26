#serializador django

from rest_framework import serializers
from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Servicio
        fields = ['nombre_servicio', 'valor_servicio', 'descripcion_servicio', 'fecha_servicio', 'tipo_servicio']
