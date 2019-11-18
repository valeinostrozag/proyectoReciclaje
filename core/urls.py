from django.urls import path, include
from .views import home, servicios, login, registro, mantenedor, agregarServicio, modificarServicio, eliminarServicio, registrar_usuario

urlpatterns = [
    path('', home, name="home"),
    path('servicios/', servicios, name="servicios"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('mantenedor/', mantenedor, name="mantenedor"), 
    path('agregarServicio/', agregarServicio, name="agregarServicio"),
    path('modificarServicio/<id>', modificarServicio, name="modificarServicio"),
    path('eliminarServicio/ <id>', eliminarServicio, name="eliminarServicio"),
    path('/accounts/', include('django.contrib.auth.urls')),
    path('registrar-usuario/', registrar_usuario, name="registrar-usuario"),
]

