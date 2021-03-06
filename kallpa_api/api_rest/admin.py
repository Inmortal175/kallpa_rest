from dis import dis
from pyexpat import model
from django.contrib import admin

from .models import dispositivo, marca, modelo, role, estado

from .Models.productos import Presentacion_Producto, Tipo_Producto
from .Models.productos import ImagenProductoPersonalizado, Imagenes_Producto

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

@admin.register(Presentacion_Producto)
class Presentacion_ProductoAdmin(admin.ModelAdmin):
  list_display = ['id']

@admin.register(Imagenes_Producto)
class Imagenes_productoAdmin(admin.ModelAdmin):
  list_display = ['id', 'Presentacion_Producto_ID', 'imagen_normal', 'imagen_miniatura']

@admin.register(ImagenProductoPersonalizado)
class ImagenProductoPersonalizadoAdmin(admin.ModelAdmin):
  list_display = ['id', 'ProductoPersonalizado_ID', 'imagen_personalizado']

@admin.register(Tipo_Producto)
class Tipo_ProductoAdmin(admin.ModelAdmin):
  list_display = ['id']

