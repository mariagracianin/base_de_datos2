from imp import source_from_cache
from datetime import datetime
import datetime as dt
from peewee import *
#import psycopg2
from Entities.cliente import Cliente
from Entities.cuenta import Cuenta
from Entities.Tarjeta import Tarjeta
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
    print("5) Ingresar pedido Simple ")
    print("6) Agregar Producto")
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
        bajaCuenta(dni1)
        borrar_cliente = Cliente.delete().where(Cliente.dni==dni1)
        borrar_cliente.execute()
        print("Baja cliente exitosa")
    except Exception:
        print("ERROR: baja cliente")

def bajaCuenta(dni1):
    try:
        borrar_cuenta = Cuenta.delete().where(Cuenta.dni_cliente==dni1)
        borrar_cuenta.execute()
        print("Baja cuenta exitosa")
    except Exception:
        print("ERROR: baja cuenta")

def modificarCliente(dni, nuevoNombre, nuevoApellido, nuevoCelular, nuevoMail, nuevoDepartamento, nuevaCalle, nuevoCodigoPostal, nuevoApartamento, nuevaLocalidad, nuevaPuerta, nuevo_usuario):
    #query = Cliente.update({Cliente.celular:nuevoCelular, Cliente.mail:nuevoMail, Cliente.nombre:nuevoNombre, Cliente.apellido:nuevoApellido, Cliente.departamento:nuevoDepartamento,Cliente.apartamento:nuevoApartamento,Cliente.calle:nuevaCalle,Cliente.codigo_postal:nuevoCodigoPostal,Cliente.localidad:nuevaLocalidad,Cliente.numero_puerta:nuevaPuerta}).where(Cliente.dni==dni)
    query = Cliente.update({Cliente.celular:nuevoCelular}).where(Cliente.dni==dni)

def ingresarStock(codigo_producto, stock ,precio = None, nombre = None, qr = "1"):
    if (Producto.get(Producto.codigo_producto == codigo_producto) == None):
        neuvoProducto = Producto.create(codigo_producto = codigo_producto, precio = precio, nombre = nombre, stock = stock, qr = qr)
    else:
        (Producto.get(Producto.codigo_producto == codigo_producto)).stock = stock + (Producto.get(Producto.codigo_producto == codigo_producto))

def altaPedidoProducto(cantidad, codigo_producto, id_pedido_simple):
    nuevoPedidoProducto = productosPedido(cantidad = cantidad, codigo_producto = codigo_producto, id_pedido_simple = id_pedido_simple)

def altaPedidoSimple(estado, fecha, canalDeCompra, dnicliente, nro_pedido_compuesto = None ):
    pedidoSimple = PedidoSimple.create(precio_total = 0, estado = estado, fecha = fecha, canal_de_compra = canalDeCompra, nro_pedido_compuesto = nro_pedido_compuesto, dni_cliente = dnicliente)

    return pedidoSimple

def calcularPrecioTotal(pedidoSimple):
    listaProductos = productosPedido.get(productosPedido.id_pedido_simple == pedidoSimple.id)

    for producto in listaProductos:
        if ((Producto.get(Producto.codigo_producto == producto.codigo_producto)).stock > producto.cantidad):
            precioTotal = precioTotal + producto.precio
            (Producto.get(Producto.codigo_producto == producto.codigo_producto)).stock = (Producto.get(
                Producto.codigo_producto == producto.codigo_producto)).stock - producto.cantidad
        else:
            return "no hay suficiente stock"

    return precioTotal

#creo cliente -> creo cuenta creo tarjeta
#
if __name__ == "__main__":
    print("-----------------------------")
    db.connect()
    db.create_tables([Cliente, Cobro, Cuenta, PedidoCompuesto, PedidoSimple, Producto, productosPedido, Tarjeta])
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

        elif(menu == "5"):
            print("Haga su pedido")
            dni_cliente = input("Ingrese su DNI")
            sigo = input("Precione 1 si quiere agreagr un producto o  0 si ya termino su pedido")

            pedido_simple = altaPedidoSimple("por confirmar", datetime.now(), "visa", dni_cliente)

            cantidad_productos = 0

            while(sigo == 1 & cantidad_productos < 21):
                codigo_producto = input("Numero del producto: ")
                cantidad_del_producto = input("Cantidad del poducto que quiere llevar")
                altaPedidoProducto( int(cantidad_del_producto), int(codigo_producto), pedido_simple )

                pedido_simple.precio_total = calcularPrecioTotal(pedido_simple)

                cantidad_productos = cantidad_productos + int(cantidad_del_producto)

                sigo = input("Precione 1 si quiere agreagr un producto o  0 si ya termino su pedido")

            if(cantidad_productos > 20):
                print("excedio la cantidad de productos posibles")
                borrar_pedido_simple = PedidoSimple.delete().where(PedidoSimple.id == pedido_simple.id)
                borrar_pedido_simple.execute()
                break

            cuenta = Cuenta.get(Cuenta.dni_cliente == dni_cliente)

            cobro = Cobro.create(id_predido = pedido_simple.id, numero_cuenta = cuenta.numero_cuenta, aprobado = False, numero_aprovacion = None)
            
            tarjeta = Tarjeta.get(Tarjeta.numero_cuenta == cuenta.numero_cuenta)
            
            if(tarjeta != None):  # hay q ver que devuelve un get que no encontro nada 
                cobro.aprobado = True
                print("Su pedido fue recivido con excito")
        
        elif(menu == 6):
            print( "Agruegue el producto que quiera agregar:")
            
            numero_producto = input ("Ingrese numero de producto: ")
            stock = input("Ingrese la cantidad de stock: ")
            
            if(Producto.get(Producto.codigo_producto == numero_producto) != None):
                ingresarStock(int(numero_producto), int(stock))

            else:
                precio = input("Ingrese precio del producto: ")
                nombre = input("Ingrese nombre del producto: ")

                ingresarStock(int(numero_producto), int(stock), int(precio), nombre)


            
            
            
            
            
            
