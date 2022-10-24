from peewee import *
from cliente import Cliente
from pedidoCompuesto import PedidoCompuesto

import psycopg2
import Principal

class PedidoSimple:
   id = BigIntegerField(primary_key=True)
   precio_total = FloatField()
   estado = CharField()
   fecha = DateField()
   canal_de_compra = CharField()
   nro_pedido_compuesto = ForeignKeyField(PedidoCompuesto, to_field="id")
   dni_cliente = ForeignKeyField(Cliente, to_field="dni")
   
   class Meta:
      database = Principal.db

