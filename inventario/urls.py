from rest_framework import routers

from .viewsets import ProveedorViewSet
from .viewsets import (CategoriaProductoViewSet,
                       AccionProductoViewSet,
                       AplicacionProductoViewSet,
                       UnidadMedidaProductoViewSet,
                       TipoProductoViewSet)
router = routers.SimpleRouter()
router.register('proveedores',ProveedorViewSet)
router.register('categoria-producto', CategoriaProductoViewSet)
router.register('accion-producto', AccionProductoViewSet)
router.register('aplicacion-producto', AplicacionProductoViewSet)
router.register('unidad-medida-producto', UnidadMedidaProductoViewSet)
router.register('tipo-producto', TipoProductoViewSet)

urlpatterns = router.urls