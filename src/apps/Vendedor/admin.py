from django.contrib import admin

from apps.Vendedor.models import Vendedor


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'correo', 'direccion')
