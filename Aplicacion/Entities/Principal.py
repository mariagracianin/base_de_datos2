from peewee import *

import psycopg2

db = PostgresqlDatabase('BaseDeDatos2', host='localhost', port=5432, user='postgres', password='Igna.soler10')

class Cuenta(Model):
   numero_cuenta = IntegerField(primary_key=True)
   usuario = CharField()
   dni = IntegerField()
   fecha_creacion = DateField()

   class Meta:
       database = db

class Producto(Model):
   codigo_producto = IntegerField(primary_key=True)
   codigo_QR = CharField()
   cantidad_stock = IntegerField()
   precio = IntegerField()
   nombre = CharField()
   
   class Meta:
      database = db

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
      database = db

class Tarjeta(Model):
   numero_tarjeta = IntegerField(primary_key=True)
   tipo = CharField()
   vencimiento = DateField()
   emisor = CharField()
   numero_cuenta = IntegerField(unique=True)

   class Meta:
      database = db

class PedidoCompuesto:
   idPedidoCompuesto = IntegerField(primary_key=True)
   dni_cliente = ForeignKeyField(Cliente, to_field="cliente-dni")
   fecha = DateField()
   canal_de_compra = CharField()

   class Meta:
      datebase = db

class PedidoSimple:
   idPedidoSimple = IntegerField(primary_key=True)
   precio_total = IntegerField()
   estado = CharField()
   fecha = DateField()
   canal_de_compra = CharField()
   numero_pedido_compuesto = ForeignKeyField(PedidoCompuesto, to_field="idPedidoCompuesto")
   dni_cliente = ForeignKeyField(Cliente, to_field="cliente_dni")
   
   class Meta:
      database = db

class Cobro(Model):
   id_pedido = ForeignKeyField(PedidoSimple, to_field="idPedidoSimple")
   numero_cuenta = IntegerField()
   aprovado = BooleanField()
   numero_aprovacion = IntegerField()

   class Meta:
      database = db


class productosPedido(Model):
   codigo_Producto_pedido = ForeignKeyField(Producto, to_field="codigo_producto")
   codigo_Producto = IntegerField(primary_key=True)
   id_pedido_simple = ForeignKeyField(PedidoSimple, to_field="idPedidoSimple")
   #id_pedido_simple = IntegerField(primary_key=True)
   cantidad = IntegerField

   class Meta:
      database = db


db.connect()
#db.create_tables([Profesores, Clases])