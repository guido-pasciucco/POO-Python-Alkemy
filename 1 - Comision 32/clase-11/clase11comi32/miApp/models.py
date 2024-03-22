from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=3)
