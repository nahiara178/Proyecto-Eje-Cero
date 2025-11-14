from django.contrib import admin

from apps.Venta_Compra.models import Venta_Compra

@admin.register(Venta_Compra)
class Venta_CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vendedor', 'producto', 'cantidad', 'precio_total', 'fecha_venta')
    search_fields = ('cliente__nombre', 'vendedor__nombre', 'producto__nombre')
    list_filter = ('fecha_venta',)
    ordering = ('-fecha_venta',)




