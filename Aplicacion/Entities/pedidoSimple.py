from peewee import *
import pedidoCompuesto
import cliente

import psycopg2
import Principal

class PedidoSimple:
   idPedidoSimple = IntegerField(primary_key=True)
   precio_total = IntegerField()
   estado = CharField()
   fecha = DateField()
   canal_de_compra = CharField()
   numero_pedido_compuesto = ForeignKeyField(pedidoCompuesto, to_field="idPedidoCompuesto")
   dni_cliente = ForeignKeyField(cliente, to_field="cliente_dni")
   
   class Meta:
      database = Principal.db
