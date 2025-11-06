from django.contrib import admin


from django.contrib import admin
from .models import Medio_pago
@admin.register(Medio_pago)
class Medio_pagoAdmin(admin.ModelAdmin):
 list_display = ['id', 'tipo_pago', 'comprobante', 'fecha', 'hora']

