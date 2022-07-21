from pydoc import describe
from django.db import models

# other import

class Evento(models.Model):
  nombre_evento      = models.CharField(max_length=255, blank=True)
  descripcion_evento = models.TextField(blank=True, null=True)
  fecha_hora_inicio  = models.DateTimeField(auto_now_add=False, null=True)
  fecha_hora_fin     = models.DateTimeField(auto_now_add=False, null=True)

  def __str__(self) -> str:
    return str(self.id)