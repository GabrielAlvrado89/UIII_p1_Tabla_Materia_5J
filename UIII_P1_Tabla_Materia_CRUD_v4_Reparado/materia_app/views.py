from django.shortcuts import render,redirect
from .models import Materia
# Create your views here.
def inicio_vista(request):
    lasmateria=Materia.objects.all()
    return  render(request,"gestionarMateria.html",{"mismateria":lasmateria})


def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarmateria=Materia.objects.create(
    codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect("/")

def seleccionarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    return render(request,'editarmateria.html', {'mismateria': materia})


def editarMateria(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']
    materia = Materia.objects.get(codigo=codigo)
    materia.nombre = nombre
    materia.creditos = creditos
    materia.save() # guarda registro actualizado
    return redirect("/")


def borrarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    materia.delete() # borra el registro
    return redirect("/")