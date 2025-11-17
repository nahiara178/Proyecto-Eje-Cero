from django.contrib import admin

from apps.Venta_Compra.models import Venta_Compra

@admin.register(Venta_Compra)
class Venta_CompraAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'id_indumentaria', 'descripción')