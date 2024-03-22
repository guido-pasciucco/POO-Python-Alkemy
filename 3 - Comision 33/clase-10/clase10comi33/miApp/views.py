from django.shortcuts import render
from .models import Usuario

# C - CREATE / CREAR
# creamos una instancia del modelo Usuario
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

# R - READ / LEER
# Listar TODOS los usuarios
def mostrar_usuarios(request):
    usuarios = Usuario.objects.all() # mostrar todas las instancias de User
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

# Filtrar por EDAD a los usuarios
def filtrar_usuarios_edad(request, edad):
    usuariosEncontrados = Usuario.objects.filter(edad = edad)
    return render(
        request,
        'usuarios_filtrados.html',
        {'usuariosEncontrados': usuariosEncontrados}
    )

# U - UPDATE / ACTUALIZAR
# actualizar usuario por ID 
def update_usuario_id(request, id, nombre, apellido, edad):
    usuarioAActualizar = Usuario.objects.get(id = id)
    usuarioAActualizar.nombre = nombre
    usuarioAActualizar.apellido = apellido
    usuarioAActualizar.edad = edad
    usuarioAActualizar.save()
    usuarios = Usuario.objects.all()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

# D - DELETE / BORRAR
# borrar un usuario por su ID
def borrar_usuario_id(request, id):
    usuarioABorrar = Usuario.objects.get(id = id)
    usuarioABorrar.delete()
    usuarios = Usuario.objects.all()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

# borrar TODo el listado
def borrar_usuarios(request):
    usuarios = Usuario.objects.all()
    usuarios.delete()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

# json 2 (alternativas)