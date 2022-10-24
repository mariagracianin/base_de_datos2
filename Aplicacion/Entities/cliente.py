from peewee import *

import psycopg2

import Principal

class Cliente(Model):
   cliente_dni = IntegerField(primary_key=True)
   celular = IntegerField()
   mail = CharField()
   nombre = CharField()
   apellido = CharField()
   departamento = CharField()
   calle = CharField()
   codigo_postal = IntegerField()
   apartament0 = IntegerField()
   localidad = CharField()
   puerta = IntegerField()

   class Meta:
      database = Principal.db