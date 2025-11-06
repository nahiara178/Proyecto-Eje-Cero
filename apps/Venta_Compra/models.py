from django.db import models

from apps import Indumentaria

class Venta_Compra (models.Model):
    fecha = models.CharField()
    hora =models.CharField()
    id_indumentaria = models.ForeignKey(Indumentaria, on_delete= models.CASCADE)
    Descripción = models.CharField()

    def __str__(self):
        return self.fecha
