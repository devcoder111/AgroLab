from djongo import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    nombre_banco = models.CharField(max_length=30)
    no_cuenta = models.CharField(max_length=20)
    nombre_vendedor = models.CharField(max_length=30)
    telefono_vendedor = models.CharField(max_length=8)

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)

class AccionProducto(models.Model):
    nombre = models.CharField(max_length=25)

class AplicacionProducto(models.Model):
    nombre = models.CharField(max_length=25)
# class AplicacionesProducto(models.Model):
#     aplicaciones = models.ArrayField(models.CharField(max_length=25))