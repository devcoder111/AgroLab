# from rest_framework import routers
#
# from .viewsets import ProveedorViewSet
# from .viewsets import (CategoriaProductoViewSet,
#                        AccionProductoViewSet,
#                        AplicacionProductoViewSet,
#                        UnidadMedidaProductoViewSet,
#                        TipoProductoViewSet,
#                        LoteViewSet,
#                        MedidasViewSet,
#                        DetalleUnitarioViewSet,
#                        PresentacionViewSet,
#                        ProductoViewSet)
#
# router = routers.SimpleRouter()
# router.register('proveedores', ProveedorViewSet)
# router.register('categoria-producto', CategoriaProductoViewSet)
# router.register('accion-producto', AccionProductoViewSet)
# router.register('aplicacion-producto', AplicacionProductoViewSet)
# router.register('unidad-medida-producto', UnidadMedidaProductoViewSet)
# router.register('tipo-producto', TipoProductoViewSet)
# router.register('lotes-producto',LoteViewSet)
# router.register('medidas-producto',MedidasViewSet)
# router.register('detalle-unitario-producto',DetalleUnitarioViewSet)
# router.register('presentaciones-producto', PresentacionViewSet)
# router.register('productos', ProductoViewSet)
#
# urlpatterns = router.urls

from django.conf.urls import url, include
from rest_framework import routers
from .apiviews import (ProveedorView,
                       CategoriaView,
                       AccionView,
                       AplicacionView,
                       UnidadMedidaView,
                       TipoProductoView,
                       ProductoView)

urlpatterns = [
    url(r'^proveedor-producto/$', ProveedorView.as_view()),
    url(r'^proveedor-producto/(?P<pk>[a-zA-Z0-9-]+)/$', ProveedorView.as_view()),
    url(r'^categoria-producto/$', CategoriaView.as_view()),
    url(r'^categoria-producto/(?P<pk>[a-zA-Z0-9-]+)/$', CategoriaView.as_view()),
    url(r'^accion-producto/$', AccionView.as_view()),
    url(r'^accion-producto/(?P<pk>[a-zA-Z0-9-]+)/$', AccionView.as_view()),
    url(r'^aplicacion-producto/$', AplicacionView.as_view()),
    url(r'^aplicacion-producto/(?P<pk>[a-zA-Z0-9-]+)/$', AplicacionView.as_view()),
    url(r'^unidad-medida-producto/$', UnidadMedidaView.as_view()),
    url(r'^unidad-medida-producto/(?P<pk>[a-zA-Z0-9-]+)/$', UnidadMedidaView.as_view()),
    url(r'^tipo-producto/$', TipoProductoView.as_view()),
    url(r'^tipo-producto/(?P<pk>[a-zA-Z0-9-]+)/$', TipoProductoView.as_view()),
    url(r'^producto/$', ProductoView.as_view()),
    url(r'^producto/(?P<pk>[a-zA-Z0-9-]+)/$', ProductoView.as_view())
]
