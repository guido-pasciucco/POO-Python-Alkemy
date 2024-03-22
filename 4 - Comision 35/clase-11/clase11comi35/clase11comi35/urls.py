from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miApp.urls'))
]

# crear un SUPERUSUARIO.
# el primer usuario que se genera y que tiene todos los 
# permisos habilitados.
# staff 