from peewee import *

import psycopg2
from Entities.pedidoSimple import PedidoSimple
from Entities.cuenta import Cuenta
from Entities.database import *


class Cobro(BaseModel):
   id_pedido = ForeignKeyField(PedidoSimple, to_field="id", primary_key=True)
   numero_cuenta = ForeignKeyField(Cuenta, to_field="numero_cuenta")
   aprobado = BooleanField()
   nro_aprovacion = BigIntegerField()