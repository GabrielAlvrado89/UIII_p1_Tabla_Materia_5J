from django.urls import path
from sucursales_app import views 

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path('seleccionarSucursal/<id_sucursal>', views.seleccionarSucursal, name='seleccionarSucursal'),
    path('editarSucursal/', views.editarSucursal, name='editarMateria'),
    path('borrarSucursal/<id_sucursal>', views.borrarSucursal, name='borrarSucursal' ),
]