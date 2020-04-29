from rest_framework import serializers
from rest_meets_djongo.serializers import DjongoModelSerializer
from.models import (Proveedor,
                    CategoriaProducto,
                    AccionProducto,
                    AplicacionProducto,
                    UnidadMedidaProducto,
                    TipoProducto)

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

class AplicacionProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplicacionProducto
        fields = "__all__"

class UnidadMedidaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedidaProducto
        fields = "__all__"

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = "__all__"


# class AplicacionesProductoSerializer(DjongoModelSerializer):
#     class Meta:
#         model = AplicacionesProducto
#         fields = "__all__"

