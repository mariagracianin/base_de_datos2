from peewee import *

from Entities.producto import Producto
from Entities.pedidoSimple import PedidoSimple
from Entities.database import *

class productosPedido(BaseModel):
   codigo_producto = ForeignKeyField(Producto, to_field="codigo_producto")
   id_pedido_simple = ForeignKeyField(PedidoSimple, to_field="id")
   cantidad = IntegerField()
   pk_producto_pedido = CompositeKey("codigo_producto","id_pedido_simple")
