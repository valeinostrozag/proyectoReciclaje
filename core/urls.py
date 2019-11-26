from django.urls import path, include
from .views import home, servicios, login, registro, mantenedor, agregar_servicio, modificar_servicio, eliminar_servicio, registrar_usuario, contratar_servicio, perfil, cancelar_servicio, ServicioViewSet
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('servicio', ServicioViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('servicios/', servicios, name="servicios"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('mantenedor/', mantenedor, name="mantenedor"), 
    path('agregar-servicio/', agregar_servicio, name="agregar-servicio"),
    path('modificar-servicio/<id>/', modificar_servicio, name="modificar-servicio"),
    path('eliminar-servicio/<id>/', eliminar_servicio, name="eliminar-servicio"),
    path('/accounts/', include('django.contrib.auth.urls')),
    path('registrar-usuario/', registrar_usuario, name="registrar-usuario"),
    path('contratar-servicio/<id>/', contratar_servicio, name="contratar-servicio"),
    path('perfil/', perfil, name="perfil"),
    path('cancelar-servicio/', cancelar_servicio, name="cancelar-servicio"),
    path('api/', include(router.urls)),
    
]

