from rest_framework.viewsets import ModelViewSet

# serializers import
from ..serializers.producto_serializer import ProductoSerializer, Presentacion_ProductoSerializer
from ..serializers.producto_serializer import ProductoPersonalizadoSerializer, PrecioProductoPersonalizadoSerializer
from ..serializers.producto_serializer import Tipo_ProductoSerializer
from ..serializers.producto_serializer import Imagenes_ProductoSerializer, ImagenProductoPersonalizadoSerializer


from ..Models.productos import Producto, ProductoPersonalizado, Presentacion_Producto
from ..Models.productos import Tipo_Producto, PrecioProductoPersonalizado
from ..Models.productos import Imagenes_Producto, ImagenProductoPersonalizado


#persmisos
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from ..permissions.permissions import IsAdminOrReadOnly, IsClient

class ProductoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = ProductoSerializer
  queryset = Producto.objects.all()

  http_method_names = ['get', 'post', 'put']

class ProductoPersonalizadoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = ProductoPersonalizadoSerializer
  queryset = ProductoPersonalizado.objects.all()

  http_method_names = ['get', 'post', 'put']

class Tipo_ProductoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = Tipo_ProductoSerializer
  queryset = Tipo_Producto.objects.all()

  http_method_names = ['get', 'post', 'put']

class PrecioProductoPersonalizadoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = PrecioProductoPersonalizadoSerializer
  queryset = PrecioProductoPersonalizado.objects.all()

  http_method_names = ['get', 'post', 'put']

class Presentacion_ProductoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = Presentacion_ProductoSerializer
  queryset = Presentacion_Producto.objects.all()

  http_method_names = ['get', 'post', 'put']

class Imagenes_ProductoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = Imagenes_ProductoSerializer
  queryset = Imagenes_Producto.objects.all()

  http_method_names = ['get', 'post', 'delete']


class ImagenProductoPersonalizadoModelViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = ImagenProductoPersonalizadoSerializer
  queryset = ImagenProductoPersonalizado.objects.all()

  http_method_names = ['get', 'post', 'delete']