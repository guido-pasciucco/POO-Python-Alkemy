from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saludo1', views.saludo1),
    path('saludo2', views.saludo2),
    path('saludo3', views.saludo3),
]
