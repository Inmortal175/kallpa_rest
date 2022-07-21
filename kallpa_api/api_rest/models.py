from django.db import models

# Create your models here.


class dispositivo(models.Model):
  dispositivo = models.CharField(max_length=70, unique=True)
  es_elimidado = models.BooleanField(default=False)
  def __str__(self) -> str:
    return str(self.id)

class marca(models.Model):
  nombre_marca = models.CharField(max_length=30, unique=True)
  id_dispositivo = models.ForeignKey(dispositivo, models.CASCADE)
  es_elimidado = models.BooleanField(default=False)

  def __str__(self) -> str:
    return str(self.id)

class modelo(models.Model):
  nombre_modelo = models.CharField(max_length=30, unique=True)
  id_marca = models.ForeignKey(marca, models.CASCADE)
  es_elimidado = models.BooleanField(default=False)

  def __str__(self) -> str:
    return str(self.id)

class role(models.Model):
  role_value = models.CharField(max_length=25, unique=True)

  def __str__(self) -> str:
    return str(self.id) # return value the id from role

class estado(models.Model):
  nombre_estado = models.CharField(max_length=25, unique=True)
  describe = models.CharField(max_length=255)

  def __str__(self):
    return str(self.id) # return value the id from status