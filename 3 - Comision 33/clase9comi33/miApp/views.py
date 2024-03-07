from django.shortcuts import render
from .models import Usuario

# Create your views here.
# CRUD - Create, Read, Update, Delete
# CRUD - Crear, Leer, Actualizar, Borrar - Datos

def crear_usuario(request):
    # asignarle directamente los valores a la instancia
    usuario = Usuario.objects.create(
        nombre = "Marcos",
        apellido = " ",
        dni = "1237",
        edad = 24
    )
    return render(request, 'usuarios.html', {'usuario': usuario})