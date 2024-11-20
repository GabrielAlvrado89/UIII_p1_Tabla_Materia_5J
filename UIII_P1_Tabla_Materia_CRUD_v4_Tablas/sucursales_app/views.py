from django.shortcuts import render,redirect
from .models import sucursales
# Create your views here.
def inicio_vista(request):
    sucursal=sucursales.objects.all()
    return  render(request,"gestionarsucursales.html",{"misucursal":sucursal})

def registrarSucursal(request):
    id_sucursal=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    Direccion=request.POST["txtdireccion"]
    NumTelefono=request.POST["NumTel"]
    creditos=request.POST["txtcreditos"]
    correo=request.POST["txtcorreo"]
    Horario=request.POST["txthorario"]

    guardarSucursal=sucursales.objects.create(
    id_sucursal=id_sucursal, nombre=nombre, Direccion=Direccion, NumTelefono=NumTelefono,
    creditos=creditos, correo=correo, Horario=Horario)
    return redirect("/")

def seleccionarSucursal(request, id_sucursal):
    sucursal = sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request,'editarsucursales.html', {'misucursal': sucursal})


def editarSucursal(request):
    id_sucursal=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    Direccion=request.POST["txtdireccion"]
    NumTelefono=request.POST["NumTel"]
    creditos=request.POST["txtcreditos"]
    correo=request.POST["txtcorreo"]
    Horario=request.POST["txthorario"]
    sucursal = sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre = nombre
    sucursal.Direccion = Direccion
    sucursal.NumTelefono = NumTelefono
    sucursal.creditos = creditos
    sucursal.correo = correo
    sucursal.Horario = Horario
    sucursal.save() # guarda registro actualizado
    return redirect("/")


def borrarSucursal(request, id_sucursal):
    sucursal = sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.delete() # borra el registro
    return redirect("/")
