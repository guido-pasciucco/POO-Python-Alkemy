from django.db import models

# Create your models here.

class Usuario(models.Model):
    # definir campos (bases de datos)
    nombre = models.CharField(max_length=100) # strings
    apellido = models.CharField(max_length=100)   
    dni = models.CharField(max_length=20)
    edad = models.IntegerField() # nums enteros
    # Definimos Metadatos
    class Meta:
        # orden descendente, por nombre
        ordering = ['-nombre']
    # definimos métodos 
    def __str__(self):
        return self.nombre