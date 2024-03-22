from django.db import models

# Create your models here.
# Creá tus modelos acá
""" 
class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
 """
class Producto(models.Model):
    titulo = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    descripcion = models.CharField(
        max_length=100,
        verbose_name='Detalle'
    )
    categoria = models.CharField(
        max_length=100
    )
    color = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=10)
    # clave_foreanea = models.ForeignKey(Categoria)

    # metodos en los modelos
    def __str__(self):
        return self.titulo