from peewee import *

import psycopg2
import Principal

class Tarjeta(Model):
   numero_tarjeta = IntegerField(primary_key=True)
   tipo = CharField()
   vencimiento = DateField()
   emisor = CharField()
   numero_cuenta = IntegerField(unique=True)

   class Meta:
      database = Principal.db