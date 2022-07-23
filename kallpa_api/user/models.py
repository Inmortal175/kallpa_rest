from django.contrib.auth.models import AbstractUser

from django.db import models

# import models from api_rest 
from api_rest.models import role, estado

class User(AbstractUser):
  
  profile = models.ImageField(upload_to = 'photos/profile',blank = True)
  email = models.EmailField(max_length = 255, unique=True)
  username = models.CharField(max_length = 255, unique = True)
  password = models.CharField(max_length = 255)

  # user model
  nombres = models.CharField(max_length = 255, blank=True)
  apellido_paterno = models.CharField(max_length = 255, blank=True)
  apellido_materno = models.CharField(max_length = 255, blank=True)
  documento_identidad = models.CharField(max_length = 8, blank=True)
  celular = models.CharField(max_length = 12, blank=True)
  kallpa_punto  = models.CharField(max_length = 8, blank=True)

  # otter users
  origen_pais = models.CharField(max_length = 50, blank=True, null=True)
  fecha_nac = models.DateTimeField(editable= True, blank=True, null=True)
  fecha_ingreso = models.DateTimeField(editable=True, auto_now_add=True)
  fecha_egreso = models.DateTimeField(editable= True, null=True, blank=True)

  contrato = models.FileField(max_length =255, blank=True, null=True)# this is from pdf files
  nombre_empresa = models.CharField(max_length = 255, blank=True, null=True)
  habilidades = models.TextField(max_length=500, blank=True)
  id_estado = models.ForeignKey(estado, on_delete=models.CASCADE, blank = True, null=True)
  id_rol = models.ForeignKey(role, on_delete=models.CASCADE, blank = True, null=True) 
  es_validado = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):  
    return str(self.id)