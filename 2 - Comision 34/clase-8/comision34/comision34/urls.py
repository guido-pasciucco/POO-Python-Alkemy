from django.contrib import admin
from django.urls import path
from comision34 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludar),
    path('despedida/', views.despedida)
]
