from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrarTemplate),
    path('otro', views.mostrarOtro)
]