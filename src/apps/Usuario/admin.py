from django.contrib import admin

from apps.Usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_de_usuario', 'contraseña')