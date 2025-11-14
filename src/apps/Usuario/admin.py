from django.contrib import admin

from apps.Usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_registro',)
    ordering = ('-fecha_registro',)