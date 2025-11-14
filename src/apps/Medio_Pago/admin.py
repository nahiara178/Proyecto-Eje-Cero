from django.contrib import admin

from apps.Medio_Pago.models import Medio_pago

@admin.register(Medio_pago)
class Medio_pagoAdmin(admin.ModelAdmin):
    list_display = ('tipo_pago', 'comprobante', 'fecha', 'hora')

