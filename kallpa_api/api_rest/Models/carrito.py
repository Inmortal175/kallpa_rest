from tkinter import N
from django.db import models

#other imports
from api_rest.Models.productos import Product, ProductoPersonalizadoModel
from ..Models import Producto, ProductoPersonalizado
from user.models import User
# shopping cart models

class carrito_compra(models.Model):
  cliente_ID      = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
  fecha_registro  = models.DateTimeField(auto_now_add=True, auto_created=True)
  distribuidor_ID = models.ForeignKey(User, null=True, on_delete = models.CASCADE)

  def __str__(self) -> str:
    return str(self.id)

class detalle_carrito_compra(models.Model):
  producto_ID               = models.ForeignKey(Producto, null=True, on_delete = models.CASCADE)
  carrito_compra_ID         = models.ForeignKey(carrito_compra, null=True, on_delete = models.CASCADE)
  producto_personalizado_ID = models.ForeignKey(ProductoPersonalizado, null=True, on_delete = models.CASCADE)
  cantidad                  = models.IntegerField(null= False)
  fecha_agregado            = models.DateTimeField(auto_now_add= True, auto_created=True)
  descuento                 = models.floatField(null= True)
  punto_aplicado            = models.IntegerField(null= True)

  def __str__(self) -> str:
    return str(self.id)


