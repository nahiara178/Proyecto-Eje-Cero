from django.contrib import admin

from django.contrib import admin
from .models import Indumentaria
@admin.register(Indumentaria)
class IndumentariaAdmin(admin.ModelAdmin):
 list_display = ['id', 'Talles', 'Diseño_a_eleccion', 'Tamaño_de_estampa', 'Corte', ]


