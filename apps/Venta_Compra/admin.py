from django.contrib import admin


from django.contrib import admin
from .models import Venta_Compra
@admin.register(Venta_Compra)
class Venta_CompraAdmin(admin.ModelAdmin):
 list_display = ['fecha', 'hora', 'id_indumentaria', 'descripcion']

