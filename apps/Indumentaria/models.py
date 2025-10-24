from django.db import models

class Indumentaria (models.Model):
    id = models.IntegerField()
    Talles = models.CharField()    
    Diseño_a_elección = models.CharField()
    Tamaño_de_estampa = models.CharField()
    Corte = models.CharField()

    def __str__(self):
        return self.id