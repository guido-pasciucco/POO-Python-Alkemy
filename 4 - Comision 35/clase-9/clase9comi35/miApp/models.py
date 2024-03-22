from django.db import models

class Usuario(models.Model):
    # Definir campos
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)
    esAdmin = models.BooleanField(default=False)
    dni = models.CharField(max_length=10, default="0")
    # Defino metadatos
    class Meta:
        ordering = ['-edad']
    # Defino métodos
    def __str__(self):
        return self.name