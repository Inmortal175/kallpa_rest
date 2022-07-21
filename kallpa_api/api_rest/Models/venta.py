from django.db import models

# other imports
from user.models import User
from ..Models.pedido import Pedido
from ..models import estado

class Tipo_Comprobante(models.Model):
  codigo = models.CharField(max_length=6)
  nombre = models.CharField(max_length=150)

  def __str__(self):
    return str(self.id)

class Venta (models.Model):
  empleado_ID = models.ForeignKey(User, null=True, on_delete = models.CASCADE) # empleado quien hizo la venta
  pedido_ID = models.ForeignKey(Pedido, null=True, on_delete = models.CASCADE)
  estado_ID = models.ForeignKey(estado, null=True, on_delete = models.CASCADE) # estado en el que se encuentra la venta
  fecha_hora_venta = models.DateTimeField(auto_now_add=True, auto_created=True)
  tipo_comprobante_ID = models.ForeignKey(Tipo_Comprobante, null=True, on_delete = models.CASCADE)

  def __str__(self):
    return str(self.id)