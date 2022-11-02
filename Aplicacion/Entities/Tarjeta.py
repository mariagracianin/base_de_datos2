from peewee import *

import psycopg2
from Aplicacion.Entities.cuenta import Cuenta
from Aplicacion.Entities.database import *

class Tarjeta(BaseModel):
   numero_tarjeta = IntegerField(primary_key=True)
   tipo = CharField()
   vencimiento = DateField()
   emisor = CharField()
   numero_cuenta = ForeignKeyField(Cuenta, to_field="numero_cuenta")