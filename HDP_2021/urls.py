"""HDP_2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asignaciones.views import asignacionIndex
from usuarios.views import usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    
=======
    path('asignasionindex/',asignacionIndex, name='indexAsignacion'),

    path('usuarios/', usuarios, name='usuarios'),
>>>>>>> 867e632a680f23358525d0d9e50489e102167935
]
