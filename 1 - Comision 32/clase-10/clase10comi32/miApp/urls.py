from django.urls import path
from . import views

# vincular "links" con funciones
# este link dispara x funcion (vista)
# este otro link dispara esta otra funcion

urlpatterns = [
    path('', views.mostrar_usuarios),
    path('create/<str:inputnombre>/<str:inputapellido>/<int:inputedad>', views.crear_usuario),
    path('filter/<int:edad>', views.filtrar_usuario),
    path('update/<int:id>', views.actualizar_usuario),
    path('delete/<int:id>', views.delete_usuario),
    path('delete', views.delete_todo), 
    path('json', views.ejemplo_json_view)
]