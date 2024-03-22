from django.contrib import admin
from django.urls import path
from .views import ejemplo

urlpatterns = [
    path('saludo', ejemplo),
]