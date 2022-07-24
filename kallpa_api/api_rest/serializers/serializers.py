# Aqui se crea los serializers para la view

from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from api_rest.models import dispositivo, marca, modelo, role, estado

# from api_rest.models.evento import *

class DispositivoSerializer(ModelSerializer):
  class Meta:
    model = dispositivo
    fields = '__all__'

class MarcaSerializer(ModelSerializer):
  class Meta:
    model = marca
    fields = '__all__'
  
class ModeloSerializer(ModelSerializer):
  class Meta:
    model = modelo
    fields = '__all__' 

class RoleSerializer(ModelSerializer):
  class Meta:
    model = role
    fields = '__all__'

class EstadoSerializer(ModelSerializer):
  class Meta:
    model = estado
    fields = '__all__'