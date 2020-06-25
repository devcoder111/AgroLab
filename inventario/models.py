from mongoengine import Document, EmbeddedDocument, fields



class Proveedor(Document):
    nombre = fields.StringField(max_length=50)
    direccion = fields.StringField(max_length=100)
    telefono = fields.StringField(max_length=8)
    nombre_banco = fields.StringField(max_length=30)
    no_cuenta = fields.StringField(max_length=20)
    nombre_vendedor = fields.StringField(max_length=30)
    telefono_vendedor = fields.StringField(max_length=8)

    def __str__(self):
        return self.nombre


class CategoriaProducto(Document):
    nombre = fields.StringField(max_length=50)

    def __str__(self):
        return self.nombre


class AccionProducto(Document):
    nombre = fields.StringField(max_length=25)

    def __str__(self):
        return self.nombre

class AplicacionProducto(Document):
    nombre = fields.StringField(max_length=25)

    def __str__(self):
        return self.nombre

class UnidadMedidaProducto(Document):
    nombre = fields.StringField(max_length=25)

    def __str__(self):
        return self.nombre

class TipoProducto(Document):
    nombre = fields.StringField(max_length=25)

    def __str__(self):
        return self.nombre

class Lote(EmbeddedDocument):
    existencia = fields.IntField()
    fecha_vencimiento = fields.DateField()

class Medidas(EmbeddedDocument):
    tipo_producto = fields.StringField(max_length=20)
    unidad_medida = fields.StringField(max_length=20)
    cantidad_medida = fields.IntField()

    def __str__(self):
        return self.tipo_producto + " " + self.unidad_medida

class DetalleUnitario(EmbeddedDocument):
    cantidad_unitaria = fields.IntField()
    nombre_sub_presentacion = fields.StringField(max_length=35)
    unidad_medida = fields.StringField(max_length=20)
    precio_unidad = fields.FloatField()

    def __str__(self):
        return self.nombre_sub_presentacion

class Presentacion(EmbeddedDocument):
    nombre = fields.StringField(required=True, max_length=35)
    precio_compra = fields.FloatField(required=True)
    precio_venta = fields.FloatField(required=True)
    lotes = fields.ListField(fields.EmbeddedDocumentField(Lote),required=True)
    medidas = fields.EmbeddedDocumentField(Medidas)
    detalle_unitario = fields.ListField(fields.EmbeddedDocumentField(DetalleUnitario))

    def __str__(self):
        return self.nombre

class Producto(Document):
    nombre = fields.StringField(required=True, max_length=50)
    categoria = fields.StringField(required=True, max_length=25)
    proveedor = fields.StringField(required=True, max_length=50)
    acciones = fields.ListField(fields.StringField(required=True))
    aplicaciones = fields.ListField(fields.StringField(required=True))
    presentaciones = fields.ListField(fields.EmbeddedDocumentField(Presentacion))

    def __str__(self):
        return self.nombre
