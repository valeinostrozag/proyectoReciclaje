from django.contrib import admin
from .models import Cliente, Servicio, TipoServicio

# Register your models here.

class TipoServicioAdmin(admin.ModelAdmin):   
    list_display= ['nombreServicio', 'descripcionServicio', 'valorServicio']
    search_fields= ['nombreServicio']

class ServicioAdmin(admin.ModelAdmin):   
    list_display= ['cliente', 'tipoServicio', 'fechaServicio']
    search_fields= ['tipoServicio']

class ClienteAdmin(admin.ModelAdmin):   
    list_display= ['nombres', 'apellidos', 'correo']
    search_fields= ['nombres']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(TipoServicio, TipoServicioAdmin)
