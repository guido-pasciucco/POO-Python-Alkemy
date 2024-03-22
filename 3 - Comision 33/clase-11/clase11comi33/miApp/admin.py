from django.contrib import admin
from .models import Producto

# MODELO  -----------> modelAdmin
# python - django ---> admin SQL

# crear un modelAdmin

# ORM - OBJECT RELATIONAL MAPPING
# trabajar SQL con CLASES, MÉTODOS, PROGRAMACIÓN

class ProductoAdmin(admin.ModelAdmin):
    # establecer 2 atributos
    list_display = ['titulo', 'descripcion', 'categoria','color', 'precio']
    # qué campos tiene en cuenta para la búsqueda
    search_fields = ['titulo', 'descripcion', 'categoria','color', 'precio']

admin.site.register(Producto, ProductoAdmin)