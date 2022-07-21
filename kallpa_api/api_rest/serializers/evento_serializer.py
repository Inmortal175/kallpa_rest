from dataclasses import field
from rest_framework.serializers import ModelSerializer
from ..Models.evento import Evento

class EventoSerializer(ModelSerializer):
  class Meta:
    model = Evento
    fields = '__all__'
