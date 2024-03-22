from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_usuarios, name='mostrar_usuarios'),
    path('create/<str:nombre>/<str:apellido>/<int:edad>', views.crear_usuario, name='crear_usuario'),
    path('filter/<int:edad>', views.filtrar_usuarios_edad, name='filtrar_usuarios_edad'),
    path('update/<int:id>/<str:nombre>/<str:apellido>/<int:edad>', views.update_usuario_id, name='update_usuario_id'),
    path('delete/<int:id>', views.borrar_usuario_id),
    path('delete', views.borrar_usuarios)
]