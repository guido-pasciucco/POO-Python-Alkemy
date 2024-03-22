from django.urls import path
from .views import crear_usuario

urlpatterns = [
    path('', crear_usuario)
]