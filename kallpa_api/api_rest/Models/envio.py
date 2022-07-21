from django.db import models

# other imports
from ..models import estado
from ..Models.pedido import Pedido

class Envio(models.Model):
  pedido_ID = models.ForeignKey(Pedido, null=False, on_delete = models.CASCADE)
  estado_ID = models.ForeignKey(estado, null=False, on_delete = models.CASCADE)
  fecha_hora_empaquetado = models.DateTimeField(auto_now_add=True, null=False, auto_created=True)
  fecha_hora_envio = models.DateTimeField(null = True, editable = True, Default = None)

  def __str__(self):
    return str(self.id)