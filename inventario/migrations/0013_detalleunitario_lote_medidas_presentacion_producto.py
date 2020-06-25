# Generated by Django 2.2.12 on 2020-06-10 07:23

from django.db import migrations, models
import django.db.models.fields
import djongo.models.fields
import inventario.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_tipoproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleUnitario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_unitaria', models.IntegerField()),
                ('nombre_sub_presentacion', models.CharField(max_length=35)),
                ('unidad_medida', models.CharField(max_length=20)),
                ('precio_unidad', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existencia', models.IntegerField()),
                ('fecha_vencimiento', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_producto', models.CharField(max_length=20)),
                ('unidad_medida', models.CharField(max_length=20)),
                ('cantidad_medida', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('lotes', djongo.models.fields.ArrayField(model_container=inventario.models.Lote)),
                ('medidas', djongo.models.fields.EmbeddedField(model_container=inventario.models.Medidas, null=True)),
                ('detalle_unitario', djongo.models.fields.ArrayField(model_container=inventario.models.DetalleUnitario)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=25)),
                ('proveedor', models.CharField(max_length=50)),
                ('acciones', djongo.models.fields.ArrayField(model_container=django.db.models.fields.CharField)),
                ('aplicaciones', djongo.models.fields.ArrayField(model_container=django.db.models.fields.CharField)),
            ],
        ),
    ]
