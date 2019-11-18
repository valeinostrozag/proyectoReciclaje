from django.contrib import admin
from .models import Perfil, Servicio

# Register your models here.


class ServicioAdmin(admin.ModelAdmin):   
    list_display= ['nombre_servicio', 'valor_servicio', 'descripcion_servicio', 'fecha_servicio']
    #search_fields= ['tipoServicio']


admin.site.register(Perfil)
admin.site.register(Servicio)
