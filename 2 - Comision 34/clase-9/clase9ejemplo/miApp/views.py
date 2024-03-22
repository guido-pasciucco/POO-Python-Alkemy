from django.shortcuts import render
from .models import Producto

def crear_producto(request):
    nombre = "Test"
    descripcion = "Bio"
    precio = 1234
    producto = Producto.objects.create(
        nombre = nombre,
        descripcion = descripcion,
        precio = precio
    )
    return render(request, 'producto.html', {'producto': producto})
