from django.shortcuts import render
from Principal.models import Persona

def usuariosIndex(request):
    personas = Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request, 'usuarios.html')
