from imp import source_from_cache
from datetime import datetime
import datetime as dt
from logging import exception
from telnetlib import PRAGMA_HEARTBEAT
from peewee import *
import psycopg2
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

#db = PostgresqlDatabase('dbd2', host='localhost', port=8888, user='dbd2g5', password='dbd2#G5')
db = psycopg2.connect(database = 'dbd2', host='localhost', port=8888, user='dbd2g5', password='dbd2#G5')
db.autocommit = True
cursor = db.cursor()


def mostrarMenu():
    print("----------MENU-----------")
    print("1) Alta cliente")
    print("2) Baja cliente")
    print("3) Modificar cliente")
    print("4) Alta tarjeta")
    print("5) Agregar Producto")
    print("6) Ingresar pedido Simple ")
    print("7) Ingresar pedido Compuesto")

    print("9) Listar clientes con SQL")
    print("10) Listar clientes")
    print("11) Listar productos en stock")
    print("12) Listar pedido por estado y fechas")
    print("13) Listar pedidos entre fechas")
    print("14) Listar pedidos de un cliente dado")

    num =input("NUMERO DEL MENU: ")
    return num

def verClientesSQL():
    sql = """SELECT * FROM cliente"""
    cursor.execute(sql)
    clientes = cursor.fetchall()
    x = 1
    print("LISTADO DE CLIENTES: ")
    for cliente in clientes:
        print(str(x)+")")
        print(cliente)
        x = x + 1    


def altaCliente(dni1, nombre1, apellido1, celular1, mail1, departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1, nombre_usuario1):
    try:
        guardar_cliente = Cliente.create(dni=dni1, nombre=nombre1, apellido=apellido1, celular=celular1, mail=mail1, departamento=departamento1, calle=calle1, codigo_postal=codigo_postal1, apartamento=apartamento1, localidad=localidad1, numero_puerta=numero_puerta1)
        #guardar_cliente.exacute()
        print("Alta cliente exitosa")
        altaCuenta(dni1, nombre_usuario1)
    except Exception:
        print("ERROR: alta cliente")

    return dni1, nombre1, apellido1, celular1, mail1,departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1, nombre_usuario1

def altaCuenta(dni1, nombre_usuario1):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    try:
        guardar_cuenta = Cuenta.create(dni_cliente = dni1, usuario = nombre_usuario1, fecha_creacion = dt.date(year,month,day))
        print("Alta cuenta exitosa")
    except Exception:
        print("ERROR: alta cuenta")

def bajaCliente(dni1):
    try:
        Cliente.get_by_id(dni1)
        bajaCuenta(dni1)
        borrar_cliente = Cliente.delete().where(Cliente.dni==dni1)
        borrar_cliente.execute()
        print("Baja cliente exitosa")
    except Exception as e:
        print(e)
        print("ERROR: baja cliente")

def bajaCuenta(dni1):
    try:
        Cuenta.get(Cuenta.dni_cliente == dni1)
        borrar_cuenta = Cuenta.delete().where(Cuenta.dni_cliente==dni1)
        borrar_cuenta.execute()
        print("Baja cuenta exitosa")
    except Exception:
        print("ERROR: baja cuenta")

def altaTarjeta(numero_tarjeta1, tipo1, vencimiento1, emisor1, numero_cuenta1):
    print(vencimiento1[6:10])
    print(vencimiento1[3:5])
    print(vencimiento1[0:2])
    vencimiento1 = dt.date(int(vencimiento1[6:10]),int(vencimiento1[3:5]),int(vencimiento1[0:2]))
    try:
        guardar_tarjeta = Tarjeta.create(numero_tarjeta = numero_tarjeta1, tipo = tipo1, emisor = emisor1, numero_cuenta = numero_cuenta1, vencimiento = vencimiento1)
        print("Alta tarjeta exitosa")
    except Exception:
        print("ERROR: alta tarjeta")

def modificarCliente(dni, nuevoNombre, nuevoApellido, nuevoCelular, nuevoMail, nuevoDepartamento, nuevaCalle, nuevoCodigoPostal, nuevoApartamento, nuevaLocalidad, nuevaPuerta):
    try:
        cliente = Cliente.get(Cliente.dni==dni)
        cliente.nombre = nuevoNombre
        cliente.apellido = nuevoApellido
        cliente.celular = nuevoCelular
        cliente.mail = nuevoMail
        cliente.departamento = nuevoDepartamento
        cliente.calle = nuevaCalle
        cliente.codigo_postal = nuevoCodigoPostal
        cliente.apartamento = nuevoApartamento
        cliente.localidad = nuevaLocalidad
        cliente.numero_puerta = nuevaPuerta
        cliente.save()
        print("Modificacion exitosa")
    except:   
        print(exception)
        print("ERROR en la modificaion")

def ingresarStock(codigo_producto, stock ,precio = None, nombre = None, qr = "1"):
    if (Producto.get_or_none(Producto.codigo_producto == codigo_producto) == None):
        nuevoProducto = Producto.create(codigo_producto = codigo_producto, precio = precio, nombre = nombre, stock = stock, qr = qr)
        nuevoProducto.save()
    else:
        (Producto.get_or_none(Producto.codigo_producto == codigo_producto)).stock = stock + (Producto.get_or_none(Producto.codigo_producto == codigo_producto))

def altaPedidoProducto(cantidad, codigo_producto, id_pedido_simple):
    nuevoPedidoProducto = productosPedido.create(cantidad = cantidad, codigo_producto = codigo_producto, id_pedido_simple = id_pedido_simple)
    nuevoPedidoProducto.save()

def altaPedidoSimple(estado, fecha, canalDeCompra, dnicliente, nro_pedido_compuesto = None):
    pedidoSimple = PedidoSimple.create(precio_total = 0, estado = estado, fecha = fecha, canal_de_compra = canalDeCompra, dni_cliente = dnicliente, nro_pedido_compuesto = nro_pedido_compuesto)
    pedidoSimple.save()

    return pedidoSimple

def altaPedidoCompuesto(fecha, canalDeCompra,dni_cliente):
    pedido_compuesto = PedidoCompuesto.create(fecha = fecha, canal_de_compra = canalDeCompra, dni_cliente = dni_cliente)

def calcularPrecioTotal(pedidoSimple):
    listaProductosPedido = productosPedido.select().where(productosPedido.id_pedido_simple == pedidoSimple.id)
    precioTotal = 0

    for producto_pedido in listaProductosPedido:
        #producto = Producto.select().where(Producto.codigo_producto == producto_pedido.codigo_producto)
        producto = Producto.get(Producto.codigo_producto == producto_pedido.codigo_producto)

        if (producto.stock > producto_pedido.cantidad):

            precioTotal = precioTotal + (producto.precio)*(producto_pedido.cantidad)
            producto.stock = producto.stock - producto_pedido.cantidad
            producto.save()
        else:
            return "no hay suficiente stock"

    return precioTotal

def listarClientes():
    listClientes = Cliente.select()
    x = 1
    print("LISTADO DE CLIENTES: ")
    for cliente in listClientes:
        print(str(x)+")")
        print("DNI: " + str(cliente.dni))
        print("APELLIDO: " + str(cliente.apellido))
        print("CELULAR: " + str(cliente.celular))
        print("MAIL: " + str(cliente.mail))
        print("DEPARTAMENTO: " + str(cliente.departamento))
        print("CALLE: " + str(cliente.calle))
        print("CODIGO POSTAL: " + str(cliente.codigo_postal))
        print("APARTAMENTO: " + str(cliente.apartamento))
        print("LOCALIDAD: " + str(cliente.localidad))
        print("NUMERO PUERTA: " + str(cliente.numero_puerta))
        x = x + 1

def listarProductosEnStock():
    listProductos = Producto.select().where(Producto.stock > 0)
    x = 1
    print("LISTADO DE PRODUCTOS EN STOCK: ")
    for producto in listProductos:
        print(str(x)+")")
        print("CODIGO PRODUCTO: " + str(producto.codigo_producto))
        print("NOMBRE: " + str(producto.nombre))
        print("PRECIO: " + str(producto.precio))
        print("STOCK: " + str(producto.stock)) #esto es la disponibilidad?
        x = x + 1


def listarPedidosPorEstadoYFechas(estado, fechaInicio, fechaFin):
    fechaInicio = dt.date(int(fechaInicio[6:10]),int(fechaInicio[3:5]),int(fechaInicio[0:2]))
    fechaFin = dt.date(int(fechaFin[6:10]),int(fechaFin[3:5]),int(fechaFin[0:2]))

    listPCompuestos = PedidoCompuesto.select().where(PedidoCompuesto.fecha<fechaFin, PedidoCompuesto.fecha>fechaInicio)
    listPSimples = PedidoSimple.select().where(PedidoSimple.estado == estado, PedidoSimple.fecha<fechaFin, PedidoSimple.fecha>fechaInicio, PedidoSimple.nro_pedido_compuesto == None)
    
    x = 1
    print("LISTADO DE PEDIDOS: en X ESTADO ENTTRE T0 Y T1")
    print("-->Pedidos compuestos: ")
    for pedido in listPCompuestos:
        estado = saberEstadoPCompuesto(pedido)
        if estado == estado:
            print(str(x)+")")
            print("CODIGO P.COMPUESTO: " + str(pedido.id))
        x = x + 1

    x = 1
    print("-->Pedidos simples que no estan en ningun compuesto")
    for pedido in listPSimples:
        print(str(x)+")")
        print("CODIGO P.SIMPLE: " + str(pedido.id))
        x = x + 1


def listarPedidosPorFechas(fechaInicio, fechaFin):
    fechaInicio = dt.date(int(fechaInicio[6:10]),int(fechaInicio[3:5]),int(fechaInicio[0:2]))
    fechaFin = dt.date(int(fechaFin[6:10]),int(fechaFin[3:5]),int(fechaFin[0:2]))

    listPCompuestos = PedidoCompuesto.select().where(PedidoCompuesto.fecha<fechaFin, PedidoCompuesto.fecha>fechaInicio)
    listPSimples = PedidoSimple.select().where(PedidoSimple.fecha<fechaFin, PedidoSimple.fecha>fechaInicio, PedidoSimple.nro_pedido_compuesto == None)
    
    x = 1
    print("LISTADO DE PEDIDOS: ENTRE T0 Y T1")
    print("-->Pedidos compuestos: ")
    for pedido in listPCompuestos:
        estado = saberEstadoPCompuesto(pedido)
    
        print(str(x)+")")
        print("CODIGO P.COMPUESTO: " + str(pedido.id))
        print("ESTADO: " + str(estado))
        print("DNI CLIENTE: " + str(pedido.dni_cliente))            
        x = x + 1

    x = 1
    print("-->Pedidos simples que no estan en ningun compuesto ")
    for pedido in listPSimples:
        print(str(x)+")")
        print("CODIGO P.SIMPLE: " + str(pedido.id))
        print("ESTADO: " + str(pedido.estado))
        print("DNI CLIENTE: " + str(pedido.dni_cliente))
        x = x + 1

def listarPedidosDeCliente(dni):
    listPCompuestos = PedidoCompuesto.select().where(PedidoCompuesto.dni_cliente == dni)
    listPSimples = PedidoSimple.select().where(PedidoSimple.dni_cliente == dni, PedidoSimple.nro_pedido_compuesto == None)
    
    x = 1
    print("LISTADO DE PEDIDOS SIMPLES DEL CLIENTE: ")
    print("-->Pedidos compuestos: ")
    for pedido in listPCompuestos:
        estado = saberEstadoPCompuesto(pedido)
    
        print(str(x)+")")
        print("CODIGO P.COMPUESTO: " + str(pedido.id))
        print("ESTADO: " + str(estado))
        print("DNI CLIENTE: " + str(pedido.dni_cliente))            
        x = x + 1

    x = 1
    print("-->Pedidos simples que no estan en ningun compuesto ")
    for pedido in listPSimples:
        print(str(x)+")")
        print("CODIGO P.SIMPLE: " + str(pedido.id))
        print("ESTADO: " + str(pedido.estado))
        print("DNI CLIENTE: " + str(pedido.dni_cliente))
        x = x + 1

def saberEstadoPCompuesto(pedidoCompuesto):
    idCompuesto = pedidoCompuesto.id
    listPSimples = PedidoSimple.select().where(PedidoSimple.nro_pedido_compuesto == idCompuesto)
    size = 0
    aprobados = 0
    rechazado = False
    despachado = False
    entregado = False
    for pedidoSimple in listPSimples:
        size = size + 1
        if pedidoSimple.estado == "aprobado":
            aprobados = aprobados + 1
        elif pedidoSimple.estado == "rechazado":
            rechazado = True
        elif pedidoSimple.estado == "despachado":
            despachado = True
        elif pedidoSimple.estado == "entregado":
            entregado = True

    
    if aprobados == size:
        return "aprobado"
    elif rechazado == True:
        return "rechazado"
    elif despachado == True and entregado == False:
        return "despachado"
    elif despachado == False and entregado == True:
        return "entregado"
    else:
        return "pendiente"


if __name__ == "__main__":
    print("----------------------------------------")
    #db.connect()
    #db.create_tables([Cliente, Cobro, Cuenta, PedidoCompuesto, PedidoSimple, Producto, productosPedido, Tarjeta])
    print("SE CREO TODO BIEN")

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
            print("--->MODIFICAR CLIENTE: ")
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
            modificarCliente(dni1, nombre1, apellido1, celular1, mail1, departamento1, calle1, codigo_postal1, apartamento1, localidad1, numero_puerta1)

        elif(menu=="4"):
            print("--->ALTA TARJETA: ")
            numero_tarjeta1 = input("NUMERO TARJETA: ")
            tipo1 = input("TIPO: ")
            vencimiento1 = input("VENCIMIENTO: ")
            emisor1 = input("EMISOR: ")
            numero_cuenta1 = input("NUMERO CUENTA: ")
            altaTarjeta(numero_tarjeta1, tipo1, vencimiento1, emisor1, numero_cuenta1)

        elif(menu == "6"):
            print("--->Haga su pedido")
            dni_cliente = input("Ingrese su DNI: ")
            sigo = input("Precione 1 si quiere agreagr un producto o  0 si ya termino su pedido: ")

            day = datetime.now().day
            month = datetime.now().month
            year = datetime.now().year
            date1 = dt.date(year,month,day)

            #PedidoCompuesto.create(fecha = date1, canal_de_compra = "", dni_cliente = dni_cliente)
            #pedidoCompuesto = PedidoCompuesto.get_or_none(PedidoCompuesto.dni_cliente == dni_cliente)

            #pedido_simple = altaPedidoSimple("por confirmar", date1, "visa", dni_cliente, pedidoCompuesto.id)

            pedido_simple = altaPedidoSimple("pendiente", date1, "visa", dni_cliente)
            pedido_simple.save()

            print(str(pedido_simple.id) + "---------------------------")

            cantidad_productos = 0

            while(sigo == "1" and cantidad_productos < 21):
                codigo_producto = input("Numero del producto: ")
                cantidad_del_producto = input("Cantidad del poducto que quiere llevar: ")
                altaPedidoProducto(int(cantidad_del_producto), int(codigo_producto), pedido_simple )

                cantidad_productos = cantidad_productos + int(cantidad_del_producto)

                sigo = input("Precione 1 si quiere agreagr un producto o  0 si ya termino su pedido: ")

            pedido_simple.precio_total = calcularPrecioTotal(pedido_simple)
            pedido_simple.save()

            if(cantidad_productos > 20):
                print("excedio la cantidad de productos posibles")
                borrar_pedido_simple = PedidoSimple.delete().where(PedidoSimple.id == pedido_simple.id)
                borrar_pedido_simple.execute()
                break

            cuenta = Cuenta.get_or_none(Cuenta.dni_cliente == dni_cliente)

            cobro = Cobro.create(id_pedido = pedido_simple.id, numero_cuenta = cuenta.numero_cuenta, aprobado = False, nro_aprovacion = 0)

            tarjeta = Tarjeta.get_or_none(Tarjeta.numero_cuenta == cuenta.numero_cuenta)

            if(tarjeta != None):  # hay q ver que devuelve un get que no encontro nada
                cobro.aprobado = True
                print("Su pedido fue recivido con excito")

        elif(menu == "5"):
            print( "--->Agruegue el producto que quiera agregar:")

            numero_producto = input ("Ingrese numero de producto: ")
            stock = input("Ingrese la cantidad de stock: ")

            if(Producto.get_or_none(Producto.codigo_producto == numero_producto) != None):
                ingresarStock(int(numero_producto), int(stock))

            else:
                precio = input("Ingrese precio del producto: ")
                nombre = input("Ingrese nombre del producto: ")

                ingresarStock(int(numero_producto), int(stock), int(precio), nombre)

        elif(menu == "7"):
            dni_cliente = input("Ingrese su DNI: ")

            paso = "1"

            day = datetime.now().day
            month = datetime.now().month
            year = datetime.now().year
            date1 = dt.date(year, month, day)

            nuevoPedidoCompueto = PedidoCompuesto.create(fecha = date1, canal_de_compra = "visa", dni_cliente = int(dni_cliente))
            nuevoPedidoCompueto.save()

            while(paso == "1"):
                id_pedido_simple = input("Ingrese los pedidos simples que quiera agregar: ")

                pedidoSimple = PedidoSimple.get_or_none(PedidoSimple.id == id_pedido_simple)

                if(pedidoSimple != None):
                    pedidoSimple.nro_pedido_compuesto = nuevoPedidoCompueto.id
                    pedidoSimple.save()
                else:
                    print("No existe esta id de pedido simple")

                print(pedidoSimple.nro_pedido_compuesto)

                paso = input("ingrese 1 si quiere agregar pedidos a su pedido compuesto, 0 para terminar")

        elif(menu=="9"):
            print("--->LISTADO CLIENTES CON SQL: ")
            verClientesSQL()

        elif(menu=="10"):
            print("--->LISTAR CLIENTES")
            listarClientes()

        elif(menu=="11"):
            print("--->LISTAR PRODUCTOS EN STOCK")
            listarProductosEnStock()

        elif(menu=="12"):
            print("--->LISTAR PEDIDOS ENTRE FECHAS Y SEGUN ESTADO: ")
            print("ingrese los siguientes datos")
            estado = input("ESTADO: ")
            fechaInicio =  input("FECHA INICIO: ")
            fechaFin =  input("FECHA FIN: ")
            listarPedidosPorEstadoYFechas(estado, fechaInicio, fechaFin)

        elif(menu=="13"):
            print("--->LISTAR PEDIDOS ENTRE FECHAS: ")
            print("ingrese los siguientes datos")
            fechaInicio =  input("FECHA INICIO: ")
            fechaFin =  input("FECHA FIN: ")
            listarPedidosPorFechas(fechaInicio, fechaFin)

        elif(menu=="14"):
            print("--->LISTAR PEDIDOS DE UN CLIENTE: ")
            print("ingrese los siguientes datos")
            dni =  input("DNI: ")
            listarPedidosDeCliente(dni)
        