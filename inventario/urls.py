from rest_framework import routers

from .viewsets import ProveedorViewSet
from .viewsets import CategoriaProductoViewSet, AccionProductoViewSet, AplicacionProductoViewSet
router = routers.SimpleRouter()
router.register('proveedores',ProveedorViewSet)
router.register('categoria-producto', CategoriaProductoViewSet)
router.register('accion-producto', AccionProductoViewSet)
router.register('aplicacion-producto', AplicacionProductoViewSet)

urlpatterns = router.urls