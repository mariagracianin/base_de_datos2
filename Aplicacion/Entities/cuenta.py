from peewee import *

import psycopg2

from Entities.cliente import Cliente
from Entities.database import *

class Cuenta(BaseModel):
    numero_cuenta = BigIntegerField(primary_key=True)
    dni_cliente = ForeignKeyField(Cliente, to_field="dni")
    usuario = CharField()
    fecha_creacion = DateField()