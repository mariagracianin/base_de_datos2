from peewee import *

import psycopg2

import pedidoSimple
import cuenta 
import Principal


class Cobro(Model):
   id_pedido = ForeignKeyField(pedidoSimple, to_field="idPedidoSimple")
   numero_cuenta = ForeignKeyField(cuenta, to_field="numero_cuenta")
   aprovado = BooleanField()
   numero_aprovacion = IntegerField()

   class Meta:
      database = Principal.db