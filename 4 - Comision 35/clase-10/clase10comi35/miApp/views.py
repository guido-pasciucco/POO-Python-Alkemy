from django.shortcuts import render
from .models import Usuario

# Funciones
# CRUD
# C - CREATE / CREAR
    # CREAR USUARIO
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
    # MOSTRAR TODOS LOS USUARIOS
def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )
    # MOSTRAR FILTRO LOS USUARIOS
def filtrar_usuarios_edad(request, edad):
    usuariosFiltrados = Usuario.objects.filter(edad = edad)
    return render(
        request, 
        'usuarios_filtrados.html', 
        {'usuariosFiltrados': usuariosFiltrados}
    )

# U - UPDATE / ACTUALIZAR
    # ACTUALIZAR UN USUARIO X SU ID

def update_usuario_id(request, id, nombre, apellido, edad):
    usuario = Usuario.objects.get(id = id)
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.edad = edad
    usuario.save()
    usuarios = Usuario.objects.all()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

# D - DELETE / BORRAR
    # BORRAME TODA LA LISTA DE USUARIOS
def borrar_todo(request):
    usuarios = Usuario.objects.all()
    usuarios.delete()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )

    # BORRAR UN USUARIO X SU ID
def borrar_usuario_id(request, id):
    # lo selecciono x su id
    usuario = Usuario.objects.get(id = id)
    # lo borro
    usuario.delete()
    # "redirecciono a la lista principal"
    usuarios = Usuario.objects.all()
    return render(
        request,
        'lista_usuarios.html',
        {'usuarios': usuarios}
    )
