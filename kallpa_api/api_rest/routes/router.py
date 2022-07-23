from rest_framework.routers import DefaultRouter

from api_rest.views.views import DispositivoModelViewSet
from api_rest.views.views import ModeloModelViewSet, MarcaModelViewSet
from api_rest.views.views import RoleModelViewSet, EstadoModelViewSet

from ..views.producto_view import ProductoModelViewSet, ProductoPersonalizadoModelViewSet
from ..views.producto_view import Tipo_ProductoModelViewSet, PrecioProductoPersonalizadoModelViewSet
from ..views.producto_view import Presentacion_ProductoModelViewSet
from ..views.producto_view import Imagenes_ProductoModelViewSet, ImagenProductoPersonalizadoModelViewSet

from ..views.evento_view import EventoModelViewSet

router_root = DefaultRouter()

router_root.register(prefix='dispositivo', basename='dispositivo',viewset=DispositivoModelViewSet)
router_root.register(prefix='marca', basename='marca', viewset=MarcaModelViewSet)
router_root.register(prefix='modelo', basename='modelo', viewset=ModeloModelViewSet)

router_root.register(prefix='estado', basename='estado', viewset=EstadoModelViewSet)

router_root.register(prefix='evento', basename='evento', viewset=EventoModelViewSet)

router_root.register(prefix='role', basename='role', viewset=RoleModelViewSet)

# debajo las rutas de productos
router_root.register(prefix='producto', basename='producto', viewset=ProductoModelViewSet)
router_root.register(prefix='tipo_producto', basename='tipo producto', viewset=Tipo_ProductoModelViewSet)
router_root.register(prefix='producto_persoanlizado', basename='producto_persoanlizado', viewset=ProductoPersonalizadoModelViewSet)
router_root.register(prefix='precio_producto_personalizado', basename='precio_producto_personalizado', viewset=PrecioProductoPersonalizadoModelViewSet)
router_root.register(prefix='presentacion_Producto', basename='presentacion_producto', viewset=Presentacion_ProductoModelViewSet)
router_root.register(prefix='imagen_producto', basename='imagen_producto', viewset=Imagenes_ProductoModelViewSet)
router_root.register(prefix='imagen_producto_personalizado', basename='imagen_producto_personalizado', viewset=ImagenProductoPersonalizadoModelViewSet)
# sobre el comentario las rutas del producto

from django.urls import path, include


urlpatterns = [
  
  path('', include(router_root.urls)),
]