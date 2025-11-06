from django.contrib import admin


from django.contrib import admin
from .models import Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
 list_display = ['nombre', 'apellido', 'telefono', 'correo', 'dni', 'direccion']

