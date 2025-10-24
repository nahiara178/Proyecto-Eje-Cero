from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField()
    telefono = models.IntegerField(max_length=100)
    correo = models.CharField()
    direccion = models.CharField()

    def __str__(self):
        return self.nombre