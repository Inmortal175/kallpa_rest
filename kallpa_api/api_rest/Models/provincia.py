from django.db import models

# other imports
from ..Models.departamento import Departamento

class Provincia(models.Model):
  codigo          = models.CharField(max_length=4, unique=True, db_index=True, primary_key=True)
  departamento_ID = models.ForeignKey(Departamento, null = False, on_delete = models.CASCADE)
  provincia       = models.CharField(max_length=255)

  def __str__(self):
    return str(self.codigo)