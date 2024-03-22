from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_usuarios), # Home
    path('create/<str:nombre>/<str:apellido>/<int:edad>', views.crear_usuario), # Sección crear user
    path('filter/<int:edad>', views.filtrar_usuarios_edad),
    path('update/<int:id>', views.update_usuario_id),
    path('delete/<int:id>', views.delete_usuario_id),
    path('delete', views.delete_all),
    path('json1', views.ejemplo_json_view1),
    path('json2', views.ejemplo_json_view2)
]

# path('create/<str:inputnombre>/<str:inputapellido>/<int:inputedad>', views.crear_usuario),
""" 
path('update/<int:id>', views.actualizar_usuario),
path('delete/<int:id>', views.delete_usuario),
path('delete', views.delete_todo), 
path('json', views.ejemplo_json_view) """