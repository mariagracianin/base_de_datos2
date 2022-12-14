from tkinter import CASCADE

from peewee import *
import peewee

import psycopg2

from Entities.cliente import Cliente
from Entities.database import *

class Cuenta(BaseModel):
    numero_cuenta = AutoField()
    #numero_cuenta = BigIntegerField(primary_key=True)
    dni_cliente = ForeignKeyField(Cliente, to_field="dni", on_update=CASCADE, on_delete=CASCADE)
    usuario = CharField()
    fecha_creacion = DateField()