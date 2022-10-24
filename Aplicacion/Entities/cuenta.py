from peewee import *

import psycopg2

import Tarjeta
import cliente 
import Principal

class Cuenta(Model):
    numero_cuenta = BigIntegerField(primary_key=True)
    dni_cliente = IntegerField()
    usuario = CharField()
    fecha_creacion = DateField()
    FKCuenta_Cliente = ForeignKeyField(Tarjeta, to_field="numero_cuenta")

    class Meta:
       database = Principal.db