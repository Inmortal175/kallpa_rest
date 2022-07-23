from  rest_framework.serializers import ModelSerializer

from ..Models.productos import Producto, PrecioProductoPersonalizado, ProductoPersonalizado
from ..Models.productos import Tipo_Producto, Presentacion_Producto
from ..Models.productos import Imagenes_Producto, ImagenProductoPersonalizado

#serializers para productos
class ProductoSerializer(ModelSerializer):
  class Meta:
    model = Producto
    fields=['id','dispositivo_ID', 'marca_ID', 'modelo_ID', 'nombre_producto', 'precio', 
     'cantidad', 'descripcion', 'puntos_aplicados', 'aplica_puntos', 'cantidad_puntos', 'en_oferta',
     'descuento', 'caducidad_puntos', 'caducidad_oferta', 'envio_gratis', 'evento_ID', 
     'presentacion_Producto_ID', 'tipo_producto_ID', 'es_elimidado'] #que gran cambio

class ProductoPersonalizadoSerializer(ModelSerializer):
  class Meta:
    model = ProductoPersonalizado
    fields = ['id', 'dispositivo_ID', 'marca_ID', 'modelo_ID', 'client_ID', 
     'tipo_producto_ID', 'precio', 'es_elimidado']

#serializers para atributos de productos
class PrecioProductoPersonalizadoSerializer(ModelSerializer):
  class Meta:
    model = PrecioProductoPersonalizado
    fields = ['id', 'dispositivo_ID', 'Empleado_ID', 'precio']

class Tipo_ProductoSerializer(ModelSerializer):
  class Meta:
    model = Tipo_Producto
    fields = ['id', 'nombre_tipo', 'es_elimidado']

class Presentacion_ProductoSerializer(ModelSerializer):
  class Meta:
    model = Presentacion_Producto
    fields = '__all__'

class Imagenes_ProductoSerializer(ModelSerializer):
  class Meta:
    model = Imagenes_Producto
    fields = '__all__'

class ImagenProductoPersonalizadoSerializer(ModelSerializer):
  class Meta:
    model = ImagenProductoPersonalizado
    fields = '__all__'
