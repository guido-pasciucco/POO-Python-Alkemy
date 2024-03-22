from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_usuarios, name="Mostrar todos los usuarios"),
    path('create/<str:nombre>/<str:apellido>/<int:edad>', views.crear_usuario, name="Crear usuario"), # nombre, apellido, edad
    path('filter/<int:edad>', views.filtrar_usuarios_edad, name="Filtrar usuarios edad"), # edad
    path('update/<int:id>/<str:nombre>/<str:apellido>/<int:edad>', views.update_usuario_id, name="Actualizar usuario x id"),
    path('delete/<int:id>', views.borrar_usuario_id, name="Borrar x id"),
    path('delete', views.borrar_todo, name="borrar todo")
]