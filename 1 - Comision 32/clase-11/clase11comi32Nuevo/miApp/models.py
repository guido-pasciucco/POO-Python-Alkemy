from django.db import models

class Producto(models.Model):
    titulo = models.CharField(
        max_length=100,
        verbose_name="Producto",
        case_sensitive=False
    )
    categoria = models.CharField(max_length=100, default="default", verbose_name="CAT")
    color = models.CharField(max_length=100, blank = True, null = True)
    precio = models.IntegerField(max_length=7)
    def __str__(self):
        return self.titulo
    
