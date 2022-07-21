# Aqui estan las vistas donde se importaran los serializers

# from django.views import View
from rest_framework.viewsets import ModelViewSet
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
from api_rest.models import dispositivo, marca, modelo, role, estado
from api_rest.serializers.serializers import DispositivoSerializer, MarcaSerializer
from api_rest.serializers.serializers import ModeloSerializer, RoleSerializer, EstadoSerializer

from rest_framework.permissions import IsAuthenticated

from ..permissions.permissions import IsAdminOrReadOnly

class DispositivoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = DispositivoSerializer
  queryset = dispositivo.objects.all()
  http_method_names = ["get", "post", "put"]

class MarcaModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = MarcaSerializer
  queryset = marca.objects.all()
  http_method_names = ['get', 'post', 'put']

class ModeloModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]

  serializer_class = ModeloSerializer
  queryset = modelo.objects.all()
  http_method_names = ['get', 'post', 'put']

class RoleModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]

  serializer_class = RoleSerializer
  queryset = role.objects.all()
  http_method_names = ['get', 'post', 'put']

class EstadoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  
  serializer_class = EstadoSerializer
  queryset = estado.objects.all()

  http_method_names = ['get', 'post', 'put']

# class DispositivoViewSet(ViewSet):
#   def list(self, request):    
#     serializer = DispositivoSerializer(dispositivo.objects.all(), many = True)
#     return Response(status=status.HTTP_200_OK, data = serializer.data)

#   def retrieve(self, request, pk : int):
#     try:
#       dispositivos = DispositivoSerializer(dispositivo.objects.get(pk=pk))
#       print(dispositivos.data)
#       return Response(status=status.HTTP_200_OK, data = dispositivos.data)
#     except:
#       if status.HTTP_500_INTERNAL_SERVER_ERROR:
#         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data = {
#           'message': 'Internal Server Error',
#         })
#       elif status.HTTP_404_NOT_FOUND:
#         return Response(status=status.HTTP_404_NOT_FOUND, data = {
#           'message': 'not found',
#         })
  
#   def create(self, request):
#     serializer = DispositivoSerializer(data = request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(status=status.HTTP_200_OK, data=serializer.data)

# class DispositivoApiView(APIView):
#   def get(self, request):
#     # # datas = dispositivo.objects.all()
#     # datas = [dispositivo.dispositivo for dispositivo in dispositivo.objects.all()]
    
#     serializer = DispositivoSerializer(dispositivo.objects.all(), many = True)
#     return Response(status=status.HTTP_200_OK, data = serializer.data)
  
#   def post(self, request):
#     serializer = DispositivoSerializer(data = request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(status=status.HTTP_200_OK, data=serializer.data)