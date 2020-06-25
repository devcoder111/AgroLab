from rest_framework_mongoengine import serializers, fields as field
from rest_framework import fields
from rest_meets_djongo.serializers import DjongoModelSerializer
from .models import (Proveedor,
                     CategoriaProducto,
                     AccionProducto,
                     AplicacionProducto,
                     UnidadMedidaProducto,
                     TipoProducto,
                     Lote,
                     Medidas,
                     DetalleUnitario,
                     Presentacion,
                     Producto)


class ProveedorSerializer(serializers.DocumentSerializer):
    nombre = fields.CharField(required=True)
    direccion = fields.CharField(required=False)
    telefono = fields.CharField(required=True)
    nombre_banco = fields.CharField(required=False)
    no_cuenta = fields.CharField(required=False)
    nombre_vendedor = fields.CharField(required=False)
    telefono_vendedor = fields.CharField(required=False)

    class Meta:
        model = Proveedor
        fields = "__all__"


class CategoriaProductoSerializer(serializers.DocumentSerializer):
    nombre = fields.CharField(required=True)

    class Meta:
        model = CategoriaProducto
        fields = "__all__"


class AccionProductoSerializer(serializers.DocumentSerializer):
    nombre = fields.CharField(required=True)

    class Meta:
        model = AccionProducto
        fields = "__all__"


class AplicacionProductoSerializer(serializers.DocumentSerializer):
    nombre = fields.CharField(required=True)

    class Meta:
        model = AplicacionProducto
        fields = "__all__"


class UnidadMedidaProductoSerializer(serializers.DocumentSerializer):
    nombre = fields.CharField(required=True)

    class Meta:
        model = UnidadMedidaProducto
        fields = "__all__"


class TipoProductoSerializer(serializers.DocumentSerializer):
    nombre = fields.CharField(required=True)

    class Meta:
        model = TipoProducto
        fields = "__all__"


class LotesSerializer(serializers.EmbeddedDocumentSerializer):
    existencia = fields.IntegerField(required=True)
    fecha_vencimiento = fields.DateField(required=False)

    class Meta:
        model = Lote
        fields = "__all__"


class MedidasSerializar(serializers.EmbeddedDocumentSerializer):
    tipo_producto = fields.CharField(required=False)
    unidad_medida = fields.CharField(required=False)
    cantidad_medida = fields.IntegerField(required=False)

    class Meta:
        model = Medidas
        fields = "__all__"


class DetalleUnitarioSerializer(serializers.EmbeddedDocumentSerializer):
    cantidad_unitaria = fields.IntegerField(required=False)
    nombre_sub_presentacion = fields.CharField(required=False)
    unidad_medida = fields.CharField(required=False)
    precio_unidad = fields.FloatField(required=False)

    class Meta:
        model = DetalleUnitario
        fields = "__all__"


class PresentacionSerializer(serializers.EmbeddedDocumentSerializer):
    nombre = fields.CharField(required=True)
    precio_compra = fields.FloatField(required=True)
    precio_venta = fields.FloatField(required=True)
    lotes = fields.ListField(LotesSerializer(required=True))
    medidas = MedidasSerializar(required=False)
    detalle_unitario = fields.ListField(DetalleUnitarioSerializer(required=False))

    class Meta:
        model = Presentacion
        fields = "__all__"


class ProductoSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Producto
        fields = "__all__"


# class AplicacionesProductoSerializer(DjongoModelSerializer):
#     class Meta:
#         model = AplicacionesProducto
#         fields = "__all__"
