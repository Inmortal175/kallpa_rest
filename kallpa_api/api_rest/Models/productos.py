from django.db import models

# others imports
from ..models import dispositivo, marca, modelo
from ..Models.evento import Evento

from user.models import User #user

class Presentacion_Producto(models.Model):
  img_normal    = models.ImageField(upload_to='img/productos', blank=True)
  img_miniatura = models.ImageField(upload_to='img/productos', blank=True)
  es_elimidado  = models.BooleanField(default=False)

  def __str__(self) -> str:
    return str(self.id)

class Tipo_Producto(models.Model):
  nombre_tipo  = models.CharField(max_length=150, unique=True)
  es_elimidado = models.BooleanField(default=False)

  def __str__(self) -> str:
    return str(self.id)

class Producto(models.Model):
  dispositivo_ID   = models.ForeignKey(dispositivo, on_delete=models.CASCADE)
  marca_ID         = models.ForeignKey(marca, on_delete=models.CASCADE)
  modelo_ID        = models.ForeignKey(modelo, on_delete=models.CASCADE)
  nombre_producto  = models.CharField(max_length=255, null=False)
  descripcion      = models.TextField(null=True)
  precio           = models.FloatField(null= False)
  cantidad         = models.IntegerField(null= True)
  aplica_puntos    = models.BooleanField(default=False)
  cantidad_puntos  = models.IntegerField(null=True)
  en_oferta        = models.BooleanField(default=False)
  descuento        = models.FloatField(default=0.0)
  caducidad_puntos = models.DateTimeField(null= True, editable=True, blank=True, auto_created=False)
  caducidad_oferta = models.DateTimeField(null= True, editable=True, blank=True, auto_created=False)
  envio_gratis     = models.BooleanField(default=False)
  
  #claves foraneas
  evento_ID                = models.ForeignKey(Evento, null=True, on_delete = models.CASCADE)
  presentacion_Producto_ID = models.ForeignKey(Presentacion_Producto, null=True, on_delete = models.CASCADE)
  tipo_producto_ID         = models.ForeignKey(Tipo_Producto, null=True, on_delete = models.CASCADE)
  es_elimidado             = models.BooleanField(default=False)

  def __str__(self) -> str:
    return str(self.id)

class PrecioProductoPersonalizado(models.Model):
  dispositivo_ID   = models.ForeignKey(dispositivo, null=True, on_delete = models.CASCADE) # a que dispositivo aplica
  Empleado_ID      = models.ForeignKey(User, null=True, on_delete = models.CASCADE) # empleado quien modifico el precio
  precio           = models.FloatField(null=False, unique=True) #precio para dispositivo selecionado
  
  def __str__(self) -> str:
    return str(self.precio)

class ProductoPersonalizado(models.Model):
  dispositivo_ID   = models.ForeignKey(dispositivo,  null=True, on_delete = models.CASCADE)
  marca_ID         = models.ForeignKey(marca, null=True, on_delete = models.CASCADE)
  modelo_ID        = models.ForeignKey(modelo, null=True, on_delete = models.CASCADE)
  client_ID        = models.ForeignKey(User, null=True, on_delete = models.CASCADE) #user created client
  tipo_producto_ID = models.ForeignKey(Tipo_Producto, null=True, on_delete = models.CASCADE)
  precio           = models.ForeignKey(PrecioProductoPersonalizado, null=True, on_delete = models.CASCADE)
  created_at       = models.DateTimeField(auto_created= True, auto_now_add=True)
  es_elimidado     = models.BooleanField(default=False)
  def __str__(self) -> str:
    return str(self.id)