from django.db import models

from apps.Indumentaria.models import Indumentaria


class Venta_Compra (models.Model):
    fecha = models.CharField()
    hora =models.CharField()
    id_indumentaria = models.ForeignKey(Indumentaria, on_delete= models.CASCADE)
    descripción = models.CharField()

    def __str__(self):
        return self.fecha