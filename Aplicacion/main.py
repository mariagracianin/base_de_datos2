from imp import source_from_cache
from datetime import datetime
import datetime as dt
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

def mostrarMenu():
    print("----------MENU-----------")
    print("1) Alta cliente")
    print("2) Baja cliente")
    print("3) Modificar cliente")
    num =input("NUMERO DEL MENU: ")
    return num

def altaCliente(dni1, nombre1, apellido1, celular1, mail1, departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1, nombre_usuario1):
    try:
        guardar_cliente = Cliente.create(dni=dni1, nombre=nombre1, apellido=apellido1, celular=celular1, mail=mail1, departamento=departamento1, calle=calle1, codigo_postal=codigo_postal1, apartamento=apartamento1, localidad=localidad1, numero_puerta=numero_puerta1)
        #guardar_cliente.exacute()
        print("Alta cliente exitosa")
        altaCuenta(dni1, nombre_usuario1)
    except Exception:
        print("ERROR: alta cliente")

    return dni1, nombre1, apellido1, celular1, mail1,departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1, nombre_usuario1

def bajaCliente(dni1):
    try:
        borrar_cliente = Cliente.delete().where(Cliente.dni==dni1)
        borrar_cliente.execute()
        print("Baja cliente exitosa")
    except Exception:
        print("ERROR: baja cliente")
    return dni1

def altaCuenta(dni1, nombre_usuario1):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    try:
        guardar_cuenta = Cuenta.create(dni_cliente = dni1, usuario = nombre_usuario1, fecha_creacion = dt.date(year,month,day), numero_cuenta = 0)
        print("Alta cuenta exitosa")
    except Exception:
        print("ERROR: alta cuenta")

def modificarCliente(dni, nuevoNombre, nuevoApellido, nuevoCelular, nuevoMail, nuevoDepartamento, nuevaCalle, nuevoCodigoPostal, nuevoApartamento, nuevaLocalidad, nuevaPuerta, nuevo_usuario):
    #query2 = Cliente.update({Cliente.celular:nuevoCelular, Cliente.mail:nuevoMail, Cliente.nombre:nuevoNombre, Cliente.apellido:nuevoApellido, Cliente.departamento:nuevoDepartamento,Cliente.apartamento:nuevoApartamento,Cliente.calle:nuevaCalle,Cliente.codigo_postal:nuevoCodigoPostal,Cliente.localidad:nuevaLocalidad,Cliente.numero_puerta:nuevaPuerta}).where(Cliente.dni==dni)
    query2 = Cliente.update({Cliente.celular:nuevoCelular}).where(Cliente.dni==dni)


if __name__ == "__main__":
    print("-----------------------------")
    db.connect()
    #db.create_tables([Cliente, Cobro, Cuenta, PedidoCompuesto, PedidoSimple, Producto, productosPedido, Tarjeta])
    print("SE CREO TODO BIEN")

    #no se si hay que hacer menu???
    while(True):
        menu = mostrarMenu()
        if(menu=="1"):
            print("---> ALTA CLIENTE: ")
            print("Ingrese los siguientes datos: ")
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
            nombre_usuario1 = input("NOMBRE DE USUARIO: ")
            altaCliente(dni1, nombre1, apellido1, celular1, mail1, departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1, nombre_usuario1)
    
        elif(menu=="2"):
            print("---> BAJA CLIENTE: ")
            print("Ingrese la cedula del cliente que quiere dar de baja: ")
            dni1 = input("DNI: ")
            bajaCliente(dni1)

        elif(menu=="3"):
            print("-->MODIFICAR CLIENTE: ")
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
            nombre_usuario1 = input("NOMBRE DE USUARIO: ")
            modificarCliente(dni1, nombre1, apellido1, celular1, mail1, departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1, nombre_usuario1)
