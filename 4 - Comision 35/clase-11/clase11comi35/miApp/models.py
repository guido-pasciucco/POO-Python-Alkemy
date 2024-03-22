from django.db import models

# Create your models here.
# CREÁ TUS MODELOS ACÁ
""" class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
"""
class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, verbose_name="Detalle")
    color = models.CharField(max_length=100)
    #categoria = models.ForeignKey(Categoria)
    precio = models.IntegerField(max_length=10)
    def __str__(self):
        return self.titulo
    
