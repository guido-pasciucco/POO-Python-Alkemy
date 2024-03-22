from django.contrib import admin
from .models import Producto



class ProductoAdmin(admin.ModelAdmin):
    # 1 - crear más columnas en tu resumen de "tareas"
    list_display = ["titulo", "categoria", "color", "precio"]
    # 2 - define que columnas puedo usar para el buscador
    search_fields = ["titulo", "categoria", "color", "precio"]


admin.site.register(Producto, ProductoAdmin)

# , ProductoAdmin)

# makemigrations
# migrate

# chequar 