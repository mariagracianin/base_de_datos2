from peewee import *

import psycopg2
import Principal
import cliente 

class PedidoCompuesto:
   idPedidoCompuesto = IntegerField(primary_key=True)
   dni_cliente = ForeignKeyField(cliente, to_field="cliente-dni")
   fecha = DateField()
   canal_de_compra = CharField()

   class Meta:
      datebase = Principal.db