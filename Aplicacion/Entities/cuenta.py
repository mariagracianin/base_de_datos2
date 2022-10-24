from peewee import *

import psycopg2

import Tarjeta
import cliente 
import Principal

class Cuenta(Model):
   numero_cuenta = ForeignKeyField(Tarjeta, to_field="numero_cuenta")
   usuario = CharField()
   dni = ForeignKeyField(cliente, to_field="cliente_dni")
   fecha_creacion = DateField()

   class Meta:
       database = Principal.db