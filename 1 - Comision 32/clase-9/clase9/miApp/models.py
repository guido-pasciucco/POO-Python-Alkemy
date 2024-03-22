from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=100)

    def __str__(self):
        return self.nombre