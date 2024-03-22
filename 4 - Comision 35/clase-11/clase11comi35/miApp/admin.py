from django.contrib import admin
from .models import Producto

# modelo original
# modelAdmin - toma las propiedades del modelo original y lo adapta a el admin
# panel de admin

class ProductoAdmin(admin.ModelAdmin):
    # 2 propiedades
    list_display = ['titulo', 'descripcion', 'color', 'precio']
    search_fields = ['titulo', 'descripcion', 'color', 'precio']

""" class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
"""

admin.site.register(Producto, ProductoAdmin)
#admin.site.register(Categoria, CategoriaAdmin)