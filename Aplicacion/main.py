from imp import source_from_cache
from peewee import *
#import psycopg2
from Entities.cliente import Cliente
from Entities.cuenta import Cuenta
from Entities.cuenta import Cuenta
from Entities.tarjeta import Tarjeta
from Entities.cobro import Cobro
from Entities.pedidoCompuesto import PedidoCompuesto
from Entities.pedidoSimple import PedidoSimple
from Entities.producto import Producto
from Entities.productoPedido import productosPedido


#db = PostgresqlDatabase('BaseDeDatos2', host='localhost', port=5432, user='postgres', password='Igna.soler10')
#db = PostgresqlDatabase('BaseDeDatos2', host='192.168.56.101', port=5432, user='labuser', password='labsuer')
db = PostgresqlDatabase('dbd2', host='localhost', port=8888, user='dbd2g5', password='dbd2#G5')


def altaCliente():
    print("---> ALTA CLIENTE: ")
    print("INGRESE LOS SIGUIENTES DATOS: ")
    dni1 = input("DNI: ")
    nombre1 = input("NOMBRE: ")
    apellido1 = input("APELLIDO: ")
    celular1 = input("CELULAR: ")
    mail1 = input("MAIL: ")
    departamento1 = input("DEPARTAMENTO: ")
    calle1 = input("CALLE: ")
    codigo_postal1 = input("CODIGO POSTAL: ")
    apartamento1 = input("APARTAMENTO: ")
    localidad1 = input("LOCALIDAD: ")
    numero_puerta1 = input("NUMERO PUERTA: ")

    Cliente.create(dni=dni1, nombre=nombre1, apellido=apellido1, celular=celular1, mail=mail1, departamento=departamento1, calle=calle1, codigo_postal=codigo_postal1, apartamento=apartamento1, localidad=localidad1, numero_puerta=numero_puerta1)

    return dni1, nombre1, apellido1, celular1, mail1,departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1

def bajaCliente():
    print("---> ALTA CLIENTE: ")
    print("INGRESE DNI DEL CLIENTE QUE QUIERE DAR DE BAJA: ")
    dni1 = input("DNI: ")
    db[Cliente].delate(dni=dni1)




if __name__ == "__main__":
    db.connect()
    print("ok1")
    db.create_tables([Cliente, Cobro, Cuenta, PedidoCompuesto, PedidoSimple, Producto, productosPedido, Tarjeta])
    print("ok2")
    altaCliente()
    print("ok3")
    bajaCliente()
