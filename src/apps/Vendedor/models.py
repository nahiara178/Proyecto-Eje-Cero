from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    telefono = models.IntegerField()
    correo = models.CharField()
    direccion = models.CharField()

    def __str__(self):
        return self.nombre