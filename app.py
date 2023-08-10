from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
#Creacion y configuracion
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3307/flask_shopy_2687365'

#Crear objetos de SQLAlchemy

db = SQLAlchemy(app)
migrate = Migrate(app, 
                  db)

#modelos
class Cliente(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(100) , unique = True)
        email = db.Column(db.String(120) , unique = True)
        password = db.Column(db.String(128))
        
class Producto(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        nombre = db.Column(db.String(100) , unique = True)
        precio = db.Column(db.Numeric(precision = 10 , scale = 2))
        imagen = db.Column(db.String(100))
        
class Venta(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        fecha = db.Column(db.DateTime , default = datetime.utcnow)
        cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

class Detalle(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'))
        venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'))
        cantidad = db.Column(db.Integer)
        
        