from django.db import models

class Usuario (models.Model):
    nombre_de_usuario = models.CharField()
    contraseña = models.CharField()

    def __str__(self):
        return self.nombre_de_usuario
    
