import json
from pymongo import MongoClient

print("-----------------------------")
db = MongoClient('mongodb://localhost:27017')

mydb = db.mdbg5.pedidos

pedidoSimple = {"precio_total": 10, 
                "estado": "pendiente", 
                "fecha": "31/07/2022",
                "canal_de_compra": "wbe", 
                "dni_cliente": 1
                }

pedidoSimple2 = {"precio_total": 12, 
                "estado": "pendiente", 
                "fecha": "31/07/2022",
                "canal_de_compra": "wbe", 
                "dni_cliente": 1
                }

mydb.insert_many([pedidoSimple,pedidoSimple2])