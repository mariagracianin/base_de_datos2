import json
from pymongo import MongoClient
from datetime import datetime
import datetime as dt

print("-----------------------------")
#db = MongoClient('mongodb://localhost:27017')

#mydb = db.mdbg5.pedidos


from pymongo import MongoClient
try:
    cliente = MongoClient('mongodb://localhost:27017')
    print("Connected successfully")
except:  
    print("Could not connect to MongoDB")

mydatabase = cliente.mdbg5   #base de datos

myCollection = mydatabase.pedidos   #esquema



pedidoSimple1 = {"precio_total": 10, 
                "estado": "aprobado", 
                "fecha": datetime.today().replace(microsecond=0),
                "canal_de_compra": "web",
                "dni_cliente": 1, 
                "listaProductos": [{
                        "codigoProducto": 10,
                        "cantidad": 2}]
                }

pedidoSimple2 = {"precio_total": 10, 
                "estado": "aprobado", 
                "fecha": datetime.today().replace(microsecond=0),
                "canal_de_compra": "web",
                "dni_cliente": 1, 
                "listaProductos": [{
                        "codigoProducto": 10,
                        "cantidad": 5}]
                }

pedidoSimple3 = {"precio_total": 10, 
                "estado": "rechazado", 
                "fecha": datetime.today().replace(microsecond=0),
                "canal_de_compra": "web",
                "dni_cliente": 1, 
                "listaProductos": [{
                        "codigoProducto": 10,
                        "cantidad": 5}]
                }

pedidoCompuesto = {"fecha": datetime.today().replace(microsecond=0),
                "canal_de_compra": "web",
                "dni_cliente": 1, 
                "pedidos_simples": [pedidoSimple1, pedidoSimple2, pedidoSimple3]
                }

pedidoSimple4 = {"precio_total": 15, 
                "estado": "aprobado", 
                "fecha": datetime.today().replace(microsecond=0),
                "canal_de_compra": "web",
                "dni_cliente": 1, 
                "listaProductos": [{
                        "codigoProducto": 20,
                        "cantidad": 5}]
                }

pedidoSimple5 = {"precio_total": 20, 
                "estado": "aprobado", 
                "fecha": datetime.today().replace(microsecond=0),
                "canal_de_compra": "web",
                "dni_cliente": 1, 
                "listaProductos": [{
                        "codigoProducto": 20,
                        "cantidad": 5}]
                }

myCollection.insert_many([pedidoSimple4, pedidoSimple5])

#criteria = {"codigoProducto": 10}
#criteria = {"fecha":"noTiene"}
criteria = {"estado":"aprobado"}

pedidoList = list(myCollection.find(criteria))

for pedido in pedidoList:
    print(pedidoList)