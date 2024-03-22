from django.shortcuts import render
from .models import Producto

# Create your views here.
# (((C)))RUD - CREATE

def crear_producto(request):
    # asignarle directamente los valores a la nueva instancia de Producto
    producto = Producto.objects.create(
        nombre = "Auriculares Audio Technica",
        descripcion = "Los mejores del mundo",
        precio = 30000
    )
    return render(request, 'productos.html', {'producto': producto})