from peewee import *
from Aplicacion.Entities.cliente import Cliente
from Aplicacion.Entities.pedidoCompuesto import PedidoCompuesto
from Aplicacion.Entities.database import *

class PedidoSimple(BaseModel):
   id = BigIntegerField(primary_key=True)
   precio_total = FloatField()
   estado = CharField()
   fecha = DateField()
   canal_de_compra = CharField()
   nro_pedido_compuesto = ForeignKeyField(PedidoCompuesto, to_field="id")
   dni_cliente = ForeignKeyField(Cliente, to_field="dni")