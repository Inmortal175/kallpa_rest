from importlib.metadata import distribution
from turtle import up
from django.db import models

# other imports
from ..models import estado
from user.models import User
from ..Models.forma_pago import Forma_Pago

from ..Models.productos import Producto

class Pedido(models.Model):
  Estado_ID = models.ForeignKey(estado, null=True, blank=True, on_delete = models.CASCADE)
  cliente_ID = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE)
  distribuidor_ID = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE)
  forma_pago_ID = models.ForeignKey(Forma_Pago, null=True, blank=True, on_delete = models.CASCADE)
  pedido_creado = models.DateTimeField(auto_now_add=True, auto_created=True)
  comprobante_pago = models.ImageField(upload_to = 'img/cliente/comprobantes', blank=True, null=True)

  def __str__(self):
    return str(self.id)

class Tipo_Pedido(models.Model):
  tipo_pedido = models.CharField(max_length=150, blank=True)

  def __str__(self) -> str:
    return str(self.id)

class Detalle_Pedido(models.Model):
  pedido_ID      = models.ForeignKey(Pedido, null=False, on_delete=models.SET_NULL)
  tipo_pedido_ID = models.ForeignKey(Tipo_Pedido, null=False, on_delete=models.SET_NULL)
  producto_ID = models.ForeignKey(Producto, null=False, on_delete=models.DO_NOTHING)
  cantidad       = models.IntegerField(null=False, default= 0)
  subtotal       = models.FloatField(null=False, default= 0.0)
  descuento      = models.FloatField(null=False, default=0.0)
  punto_aplicado = models.IntegerField(null=False, default=0)
  
