from django.shortcuts import render
from Principal.models import asignacion 
# Create your views here.


def asignacionIndex(request):
    asignaciones = asignacion.objects.all()
    contexto = {
        'asignaciones':asignaciones
    }
    return render(request,'indexAsignacion.html',contexto)

def crearAsignacion(request):
    return render(request,'crearAsignacion.html')

