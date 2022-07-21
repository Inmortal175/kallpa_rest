from django.db import models

# other imports
from ..Models.departamento import Departamento
from ..Models.provincia import Provincia

class Distrito(models.Model):
  codigo          = models.CharField(max_length=6, unique=True, db_index=True, primary_key=True)
  departamento_ID = models.ForeignKey(Departamento, null = False, on_delete = models.CASCADE)
  provincia_ID    = models.ForeignKey(Provincia, null = False, on_delete = models.CASCADE)
  distrito        = models.CharField(max_length=255)

  def __str__(self) -> str:
    return str(self.codigo)