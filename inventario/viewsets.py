from rest_framework import viewsets

from .models import (Proveedor,
                     CategoriaProducto,
                     AccionProducto,
                     AplicacionProducto,
                     UnidadMedidaProducto,
                     TipoProducto)

from .serializer import (ProveedorSerializer,
                         CategoriaProductoSerializer,
                         AccionProductoSerializer,
                         AplicacionProductoSerializer,
                         UnidadMedidaProductoSerializer,
                         TipoProductoSerializer)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class AccionProductoViewSet(viewsets.ModelViewSet):
    queryset = AccionProducto.objects.all()
    serializer_class = AccionProductoSerializer

class AplicacionProductoViewSet(viewsets.ModelViewSet):
    queryset = AplicacionProducto.objects.all()
    serializer_class = AplicacionProductoSerializer

class UnidadMedidaProductoViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedidaProducto.objects.all()
    serializer_class = UnidadMedidaProductoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer




# class AplicacionesProductoViewSet(viewsets.ModelViewSet):
#     queryset = AplicacionesProducto.objects.all()
#     serializer_class = AplicacionesProductoSerializer