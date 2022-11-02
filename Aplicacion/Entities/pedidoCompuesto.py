from peewee import *

import psycopg2
from Entities.cliente import Cliente
from Entities.database import *

class PedidoCompuesto(BaseModel):
   id = AutoField()
   fecha = DateField()
   canal_de_compra = CharField()
   dni_cliente = ForeignKeyField(Cliente, to_field="dni")
