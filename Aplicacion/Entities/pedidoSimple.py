from peewee import *
from Entities.cliente import Cliente
from Entities.pedidoCompuesto import PedidoCompuesto
from Entities.database import *

class PedidoSimple(BaseModel):
   id = AutoField()
   precio_total = FloatField()
   estado = CharField()
   fecha = DateField()
   canal_de_compra = CharField()
   nro_pedido_compuesto = ForeignKeyField(PedidoCompuesto, to_field="id")
   dni_cliente = ForeignKeyField(Cliente, to_field="dni", null = True) # revidar si esta bien
