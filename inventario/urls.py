from rest_framework import routers

from .viewsets import ProveedorViewSet
from .viewsets import CategoriaProductoViewSet

router = routers.SimpleRouter()
router.register('proveedores',ProveedorViewSet)
router.register('categorias-producto', CategoriaProductoViewSet)

urlpatterns = router.urls