from rest_framework.viewsets import ModelViewSet

from ..permissions.permissions import IsAdminOrReadOnly

from ..serializers.evento_serializer import EventoSerializer

from ..Models.evento import Evento

class EventoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = EventoSerializer
  queryset = Evento.objects.all()

  http_method_names = ['get', 'post', 'put']