from django.shortcuts import render
from .models import Persona

def usuariosIndex(request):
    personas = Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request, 'usuarios.html')
