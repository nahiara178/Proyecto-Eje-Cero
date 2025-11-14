from django.contrib import admin

from apps.Cliente.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'dni', 'direccion')
