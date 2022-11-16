import json

from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27107")

mydb = db.mbg5.pedidos

def generarJSONproductoCantidad(codigoProducto, cantidad):
    productoCantidad = {"codigoProducto": codigoProducto, "cantidad": cantidad}
    jsonProducto = json.dumps(productoCantidad, indent = 4)

    return jsonProducto

def generadorPedidoSimple(precio, estado,canal_de_compra, nro_pedido_dompuesto, dni_cliente, listaProductos ):

    pedidoSimple = {"precio_total": precio, "estado": estado, "fecha": "31/07/2022", "canal_de_compra": canal_de_compra, "nro_pedido_compuesto":nro_pedido_dompuesto, "dni_cliente": dni_cliente}
    jsonString = json.dumps(pedidoSimple, indent=4)
    mydb.insert_one(jsonString)


mydb.insert_one
#mydb.insert_one(jsonString)


