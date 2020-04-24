from rest_framework import routers

from .viewsets import ProveedorViewSet

router = routers.SimpleRouter()
router.register('proveedores',ProveedorViewSet)

urlpatterns = router.urls