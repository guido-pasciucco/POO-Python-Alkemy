from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ejemplo', views.ejemplo_plantilla )
]