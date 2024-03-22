from django.shortcuts import render
from .models import Usuario
from django.http import JsonResponse

# CRUD 

# C - CREATE - CREAR
def crear_usuario(request, nombre, apellido, edad):
    nuevo_usuario = Usuario.objects.create(
        nombre = nombre,
        apellido = apellido,
        edad = edad
    )
    return render(
        request, 
        'nuevo_usuario.html', 
        {'nuevo_usuario': nuevo_usuario}
    )

# R - READ - LEER 

# Mostrar todos los usuarios
def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(
        request, 
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

# Mostrar usuarios con filtro
def filtrar_usuarios_edad(request, edad):
    userEncontrado = Usuario.objects.filter(edad = edad)
    return render(
        request,
        'user_filtrados.html',
        {'userEncontrado': userEncontrado}
    )

# U - UPDATE - ACTUALIZAR
# actualizar usuario por su ID
def update_usuario_id(request, id):
    userAActualizar = Usuario.objects.get(id = id)
    userAActualizar.nombre = "Carlos"
    userAActualizar.apellido = "Smith"
    userAActualizar.edad = 18
    userAActualizar.save()
    return render(
        request,
        'user_actualizado.html',
        {'userAActualizar': userAActualizar}
    )

# D - DELETE - BORRAR

# borrar TODOS los usuarios
def delete_all(request):
    usuarios = Usuario.objects.all()
    usuarios.delete()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


# borrar un usuario por su ID
def delete_usuario_id(request, id):
    userABorrar = Usuario.objects.get(id = id)
    userABorrar.delete()
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


# JSON
# CONVERTIR ALGO A FORMATO JSON

# UN HTML DONDE GUARDAMOS EN .JSON TODA NUESTRA LISTA DE USUARIOS



def ejemplo_json_view1(request):
    # Crear un diccionario con datos que quieres devolver en formato JSON
    data = {
        'mensaje': 'Hola desde JsonResponse!',
        'numero': 42
    }
    return JsonResponse(data)


def ejemplo_json_view2(request):
    data = list(Usuario.objects.values('nombre', 'apellido', 'edad'))
    return render(request, 'json.html', {'data': data})