from django.db import models

# creamos modelo Usuario
class Usuario(models.Model):
    # CAMPOS
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)