from django.shortcuts import render, redirect
from .models import Usuario
from django.http import JsonResponse

# Create
def crear_usuario(request, inputnombre, inputapellido ,inputedad):
    nuevoUsuario = Usuario.objects.create(
        nombre = inputnombre,
        apellido = inputapellido,
        edad = inputedad
    )
    nuevoUsuario.save()
    return render(request, 'usuarios.html', {'nuevoUsuario': nuevoUsuario})

# Read
def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'allUsers.html', {'usuarios': usuarios})
def filtrar_usuario(request, edad):
    datosFiltrados = Usuario.objects.filter(edad = edad)
    return render(request, 'usersFiltrados.html', {'datosFiltrados': datosFiltrados})

# Update - Modificar intancias
def actualizar_usuario(request, id):
    userAActualizar = Usuario.objects.get(id=id)
    userAActualizar.nombre = "Marcos"
    userAActualizar.save()
    return render(request, 'updatedUser.html', {'updatedUser': userAActualizar})

# Delete - Eliminar Instancia por ID
def delete_usuario(request, id):
    userABorrar = Usuario.objects.get(id = id) # igual a actualizar_usuario()
    userABorrar.delete() # funcion nativa de PY
    # igual a mostrar_usuarios()
    usuarios = Usuario.objects.all()
    return render(request, 'allUsers.html', {'usuarios': usuarios})

# Delete - Eliminar Todo 
def delete_todo(request):
    usuarios = Usuario.objects.all()
    usuarios.delete()
    return render(request, 'allUsers.html', {'usuarios': usuarios})

# JSON Response - DEVUELVE UN JSON

# HTML con un JSON con todos los usuarios creados 
def ejemplo_json_view(request):
    data = list(Usuario.objects.values('nombre', 'apellido', 'edad'))
    return render(request, 'json.html', {'data': data})