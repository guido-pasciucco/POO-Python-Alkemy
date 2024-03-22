from django.urls import path
from .views import crear_producto

urlpatterns = [
    path('', crear_producto, name="Crear Producto"),
]