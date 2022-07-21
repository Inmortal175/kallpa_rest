from django.db import models

# other imports

class Forma_Pago(models.Model):
  forma_de_pago = models.CharField(max_length=50, blank=True)

  def __str__(self):
    return str(self.id)