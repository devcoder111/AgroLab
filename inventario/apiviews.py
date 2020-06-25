from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from bson import ObjectId
from django.http import Http404
from .models import (Proveedor,
                     CategoriaProducto,
                     AccionProducto,
                     AplicacionProducto,
                     UnidadMedidaProducto,
                     TipoProducto,
                     Producto)

from .serializer import (ProveedorSerializer,
                         CategoriaProductoSerializer,
                         AccionProductoSerializer,
                         AplicacionProductoSerializer,
                         UnidadMedidaProductoSerializer,
                         TipoProductoSerializer,
                         ProductoSerializer)


class ProveedorView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            proveedor = self.get_object(pk)
            serializer = ProveedorSerializer(proveedor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            proveedor = Proveedor.objects.all()
            serializer = ProveedorSerializer(proveedor, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        proveedor = self.get_object(pk)
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriaView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            categoria = self.get_object(pk)
            serializer = CategoriaProductoSerializer(categoria)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            categoria = CategoriaProducto.objects.all()
            serializer = CategoriaProductoSerializer(categoria, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return CategoriaProducto.objects.get(pk=pk)
        except CategoriaProducto.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = CategoriaProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        categoria = self.get_object(pk)
        serializer = CategoriaProductoSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccionView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            accion = self.get_object(pk)
            serializer = AccionProductoSerializer(accion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            accion = AccionProducto.objects.all()
            serializer = AccionProductoSerializer(accion, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return AccionProducto.objects.get(pk=pk)
        except AccionProducto.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = AccionProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        accion = self.get_object(pk)
        serializer = AccionProductoSerializer(accion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        accion = self.get_object(pk)
        accion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AplicacionView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            aplicacion = self.get_object(pk)
            serializer = AplicacionProductoSerializer(aplicacion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            aplicacion = AplicacionProducto.objects.all()
            serializer = AplicacionProductoSerializer(aplicacion, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return AplicacionProducto.objects.get(pk=pk)
        except AplicacionProducto.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = AplicacionProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        aplicacion = self.get_object(pk)
        serializer = AplicacionProductoSerializer(aplicacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        aplicacion = self.get_object(pk)
        aplicacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UnidadMedidaView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            unidad_medida = self.get_object(pk)
            serializer = UnidadMedidaProductoSerializer(unidad_medida)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            unidad_medida = UnidadMedidaProducto.objects.all()
            serializer = UnidadMedidaProductoSerializer(unidad_medida, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return UnidadMedidaProducto.objects.get(pk=pk)
        except UnidadMedidaProducto.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = UnidadMedidaProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        unidad_medida = self.get_object(pk)
        serializer = UnidadMedidaProductoSerializer(unidad_medida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        unidad_medida = self.get_object(pk)
        unidad_medida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TipoProductoView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            tipo_producto = self.get_object(pk)
            serializer = TipoProductoSerializer(tipo_producto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            tipo_producto = TipoProducto.objects.all()
            serializer = TipoProductoSerializer(tipo_producto, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return TipoProducto.objects.get(pk=pk)
        except TipoProducto.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = TipoProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        tipo_producto = self.get_object(pk)
        serializer = TipoProductoSerializer(tipo_producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        tipo_producto = self.get_object(pk)
        tipo_producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductoView(APIView):

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            producto = self.get_object(pk)
            serializer = ProductoSerializer(producto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            presentacion = Producto.objects.all()
            serializer = ProductoSerializer(presentacion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def post(self, request, pk=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
