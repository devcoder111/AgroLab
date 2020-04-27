from rest_framework import serializers
from rest_meets_djongo.serializers import DjongoModelSerializer
from.models import Proveedor, CategoriaProducto, AccionProducto

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = "__all__"

class AccionProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccionProducto
        fields = "__all__"


# class AplicacionesProductoSerializer(DjongoModelSerializer):
#     class Meta:
#         model = AplicacionesProducto
#         fields = "__all__"

