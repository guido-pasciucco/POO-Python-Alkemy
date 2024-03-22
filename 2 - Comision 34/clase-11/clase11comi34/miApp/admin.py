from django.contrib import admin
from .models import Producto

# Register your models here.
# inscribirlos en el gestor del admin para poder usarlo desde ahí

# modelAdmin 
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descripcion", "categoria", "color", "precio"]
    search_fields = ["titulo", "descripcion", "categoria", "color", "precio"]

admin.site.register(Producto, ProductoAdmin)
