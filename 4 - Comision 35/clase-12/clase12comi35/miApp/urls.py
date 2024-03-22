from django.urls import path
from . import views

urlpatterns = [
    path('saludo', views.saludo),
    path('lista', views.lista_estudiantes)
]
