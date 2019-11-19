from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

TIPO_DOMICILIO = (
('Fundacion', 'Fundacion'),
('Empresa', 'Empresa'),
('Casa particular', 'Casa particular'),
('Centro educacional', 'Centro educacional')
)

TIPO_RETIRO = (
('Primera semana', 'Primera semana'),
('Quincenal', 'Quincenal'),
('Fin de mes', 'Fin de mes'),
)

class Perfil(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion      = models.CharField(max_length=200)
    comuna         = models.CharField(max_length=200)
    ciudad         = models.CharField(max_length=200)
    tipo_domicilio = models.CharField(max_length=100, choices=TIPO_DOMICILIO)
    
    def __str__(self):
        return self.user.username


class Servicio(models.Model):
    nombre_servicio         = models.CharField(max_length=80)
    valor_servicio          = models.IntegerField()
    descripcion_servicio    = models.TextField(max_length=200)
    fecha_servicio          = models.CharField(max_length=100, choices=TIPO_RETIRO)
    cliente                 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre_servicio
