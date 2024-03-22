from .models import Usuario
from django.shortcuts import render

# Crea instancias de USUARIO - CREA USUARIOS

def crear_usuario(request):
    nombre = "Pepe"
    edad = 23
    esAdmin = False 
    usuario = Usuario.objects.create(
        nombre = nombre,
        edad = edad,
        esAdmin = esAdmin,
        dni = 12345
    )
    return render(request, 'usuarios.html', {'usuarios': usuario})