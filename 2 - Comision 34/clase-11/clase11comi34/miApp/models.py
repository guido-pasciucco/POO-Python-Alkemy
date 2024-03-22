from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(
        max_length=100,
        blank = True,
        null = True
    )
    categoria = models.CharField(
        max_length=100,
        default = "Sin categoría"
    )
    color = models.CharField(
        max_length=100
    )
    precio = models.IntegerField(
        max_length=7,
        default = 0
    )
    # mas tarde hacemos el método __str__
    def __str__(self):
        return self.titulo
