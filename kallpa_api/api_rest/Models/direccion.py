from django.db import models

# other imports
from user.models import User
from ..Models.departamento import Departamento
from ..Models.provincia import Provincia
from ..Models.distrito import Distrito


class Direccion(models.Model):
  cliente_ID          = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
  codigo_departamento = models.ForeignKey(Departamento, null = False, on_delete = models.CASCADE)
  codigo_provincia    = models.ForeignKey(Provincia, null = False, on_delete = models.CASCADE)
  codigo_distrito     = models.ForeignKey(Distrito, null = False, on_delete = models.CASCADE)
  direccion           = models.CharField(max_length=255, null = True)
  nro_lote            = models.CharField(max_length=255, null = True)
  urbanizacion        = models.CharField(max_length=255, null = True)
  referencia          = models.CharField(max_length=255, null = True)
  es_predeterminado   = models.BooleanField(default=False)
  distribuidor_ID     = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
  
  def __str__(self):
    return str(self.id)