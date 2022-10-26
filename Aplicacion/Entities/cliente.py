from peewee import *

import psycopg2
from Entities.database import *

class Cliente(BaseModel):
   dni = IntegerField(primary_key=True)
   nombre = CharField()
   apellido = CharField()
   celular = CharField()
   mail = CharField()
   departamento = CharField()
   calle = CharField()
   codigo_postal = CharField()
   apartamento = CharField()
   localidad = CharField()
   numero_puerta = CharField()
