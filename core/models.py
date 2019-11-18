from django.db import models
from datetime import datetime

# Create your models here.

class Cliente(models.Model):
    nombres= models.CharField(max_length=80)
    apellidos= models.CharField(max_length=80)
    correo= models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    comuna= models.CharField(max_length=80)
    cuidad= models.CharField(max_length=80)
    tipoDomicilio= models.CharField (max_length=80)
    contraseña= models.CharField(max_length=80)

    def __str__(self):
        return self.nombres

class TipoServicio(models.Model):
    nombreServicio= models.CharField(max_length=80)
    valorServicio= models.IntegerField()
    descripcionServicio= models.CharField(max_length=200)

    def __str__(self):
        return self.nombreServicio

class Servicio(models.Model):
    fechaServicio= models.DateTimeField()
    cliente= models.ForeignKey(Cliente, on_delete= models.CASCADE)
    tipoServicio= models.ForeignKey(TipoServicio, on_delete= models.CASCADE)

