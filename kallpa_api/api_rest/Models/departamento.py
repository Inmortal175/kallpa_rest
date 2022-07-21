from django.db import models

# other imports

class Departamento(models.Model):
  codigo       = models.CharField(max_length=2, unique=True, db_index=True, primary_key=True)
  departamento = models.CharField(max_length=255, unique=True)
  
  def __str__(self):
    return str(self.codigo)