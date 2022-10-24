from peewee import *
import producto
import pedidoSimple

import psycopg2
import Principal

class productosPedido(Model):
   codigo_Producto_pedido = ForeignKeyField(producto, to_field="codigo_producto")
   codigo_Producto = IntegerField(primary_key=True)
   id_pedido_simple_pedido = ForeignKeyField(pedidoSimple, to_field="idPedidoSimple")
   #id_pedido_simple = IntegerField(primary_key=True)
   cantidad = IntegerField

   class Meta:
      database = Principal.db
