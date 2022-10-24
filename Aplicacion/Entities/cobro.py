from peewee import *

import psycopg2
import Principal

from pedidoSimple import PedidoSimple
from cuenta import Cuenta


class Cobro(Model):
   id_pedido = ForeignKeyField(PedidoSimple, to_field="id", primary_key=True)
   numero_cuenta = ForeignKeyField(Cuenta, to_field="numero_cuenta")
   aprobado = BooleanField()
   nro_aprovacion = BigIntegerField()

   class Meta:
      database = Principal.db