from peewee import *

import psycopg2
import Principal

class Producto(Model):
   codigo_producto = IntegerField(primary_key=True)
   codigo_QR = CharField()
   cantidad_stock = IntegerField()
   precio = IntegerField()
   nombre = CharField()
   
   class Meta:
      database = Principal.db