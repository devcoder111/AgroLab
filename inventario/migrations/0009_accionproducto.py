# Generated by Django 2.2.12 on 2020-04-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_delete_accionproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccionProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
    ]