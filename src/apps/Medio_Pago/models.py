from django.db import models

class Medio_pago (models.Model):
    tipo_pago =  models.CharField()
    comprobante = models.CharField()
    fecha = models.CharField()
    hora = models.CharField()

    def __str__(self):
        return self.tipo_pago
