from django.contrib import admin
from .models import Persona
from .models import usuario
from .models import administrador
from .models import zona 
from .models import asignacion
from .models import paqueteAlimentario
# Register your models here.

admin.site.register(Persona)
admin.site.register(usuario)
admin.site.register(administrador)
admin.site.register(zona)
admin.site.register(asignacion)
admin.site.register(paqueteAlimentario)
