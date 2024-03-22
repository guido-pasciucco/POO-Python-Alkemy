from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # cuando entres en :8000/admin - se te va a abrir
    # el panel de administrador
    path('admin/', admin.site.urls),
    path('', include('miApp.urls'))
]
