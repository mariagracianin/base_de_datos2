from peewee import *
from Entities.database import *

class Producto(BaseModel):
   codigo_producto = BigIntegerField(primary_key=True)
   nombre = CharField()
   precio = FloatField()
   stock = IntegerField()
   qr = CharField()

