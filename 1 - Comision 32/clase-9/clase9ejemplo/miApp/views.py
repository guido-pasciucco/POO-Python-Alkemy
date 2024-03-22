from django.shortcuts import render
from .models import Producto

def crear_producto(request):
    producto = Producto.objects.create(
        nombre ='Test Product',
        descripcion ='Test Description',
        precio = 11111
    )
    return render(request, 'producto.html', {'producto': producto})
