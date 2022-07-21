from dis import dis
from pyexpat import model
from django.contrib import admin

from .models import dispositivo, marca, modelo, role, estado

# Register your models here.
@admin.register(dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
  list_display = ['id', 'dispositivo', 'es_elimidado']

@admin.register(marca)
class marcaAdmin(admin.ModelAdmin):
  list_display = ['id', 'nombre_marca', 'id_dispositivo', 'es_elimidado']

@admin.register(modelo)
class modeloAdmin(admin.ModelAdmin):
  list_display = ['id', 'nombre_modelo', 'id_marca', 'es_elimidado']

@admin.register(role)
class roleAdmin(admin.ModelAdmin):
  list_display = ['id', 'role_value']

@admin.register(estado)
class estadoAdmin(admin.ModelAdmin):
  list_display = ['id', 'nombre_estado']

