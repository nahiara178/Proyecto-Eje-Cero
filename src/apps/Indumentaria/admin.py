from django.contrib import admin

from apps.Indumentaria.models import Indumentaria

@admin.register(Indumentaria)
class IndumentariaAdmin(admin.ModelAdmin):
    list_display = ('Talles', 'Diseño_a_elección', 'Tamaño_de_estampa', 'Corte',)

