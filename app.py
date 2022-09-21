# importamos las dependencias de Flask
from flask import Flask, render_template, request
# importamos el sqlite3
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('URL_DB', default='sqlite:///database/minartpy.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Providers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20))
    company_name = db.Column(db.String(60))
    document = db.Column(db.String(20))
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    city = db.Column(db.String(100))
    raw_material = db.Column(db.String(200))
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    status = db.Column(db.Boolean)

@app.get("/")
def index():
    return render_template('index.html')

@app.get("/registro-proveedor")
def provider_register():
    raw_material = ["Textiles", "Cuero", "Madera", "Piedras", "Metales", "Astas", "Cerámica", "Fibras Vegetales", "Expresión Artística (IND)", "Artesania Ceremonial y de Recoleccion (IND)"]

    return render_template('registro_proveedor.html', tipo_materia = raw_material)

@app.get("/ejemplo-pagina")
def ejemplo_pagina():

    return render_template('ejemplo-pagina.html')

@app.get("/directorio_proveedores_mf")
def directorio_mf():

    return render_template('directorio_proveedores_mf.html')

@app.get("/artesanos")
def pagina_artesanos():

    return render_template('artesanos.html')

@app.get("/proveedores")
def pagina_proveedores():

    return render_template('proveedores.html')

@app.get("/register")
def pagina_registro():

    return render_template('registro.html')

@app.get("/iniciar-sesion")
def iniciar_sesion():

    return render_template('iniciar_sesion.html')

@app.get("/directorio")
def pagina_directorio():
    data = Providers.query.all()

    return render_template('directorio.html', profiles=data)

@app.get("/institucion")
def pagina_institucion():

    return render_template('institucion.html')

@app.get("/perfil-proveedor/<int:id_proveedor>")
def perfil_proveedor(id_proveedor):
    data = Providers.query.filter_by(id=id_proveedor).first()

    return render_template('perfil_proveedor.html', profile=data)

@app.post("/provider")
def create_providers():
    provider = Providers()
    provider.first_name = request.json["nombre"]
    provider.last_name = request.json["apellido"]
    provider.company_name = request.json["nombre_empresa"]
    provider.document = request.json["documento"]
    provider.address = request.json["direccion"]
    provider.phone_number = request.json["telefono"]
    provider.city = request.json["ciudad"]
    provider.raw_material = request.json["materia_prima"]
    provider.latitude = request.json["latitude"]
    provider.longitude = request.json["longitude"]
    provider.status = True

    db.session.add(provider)
    db.session.commit()
    
    return {"id": provider.id}

if __name__ == '__main__':
    db.create_all()
    app.run('0.0.0.0', 5000, debug=True)