from django.db import models

# crear nuestro modelo de usuario
# clase/molde desde el cual creamos instancias (en el views.py)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)
