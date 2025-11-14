from django.db import models

class Cliente(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    telefono = models.IntegerField()
    correo = models.CharField()
    dni = models.CharField()
    direccion = models.CharField()

    def __str__(self):
        return self.nombre