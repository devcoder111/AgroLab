from rest_framework import viewsets

from .models import Proveedor, CategoriaProducto, AccionProducto, AplicacionProducto

from .serializer import ProveedorSerializer, CategoriaProductoSerializer, AccionProductoSerializer, AplicacionProductoSerializer

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


# class AplicacionesProductoViewSet(viewsets.ModelViewSet):
#     queryset = AplicacionesProducto.objects.all()
#     serializer_class = AplicacionesProductoSerializer