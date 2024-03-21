from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_index),
    path('otro', views.mostrar_otro),
]
