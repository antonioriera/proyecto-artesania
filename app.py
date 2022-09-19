from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def db():
    con = sqlite3.connect("minartpy.db")

    return [con.cursor(), con]

@app.get("/create-tables")
def create_tables():
    cur, _ = db()
    cur.execute("CREATE TABLE providers(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name, last_name, company_name, document, address, phone_number, city, raw_material, latitude, longitude, status)")

    return {"create": True}

@app.get("/")
def index():
    return render_template('index.html')

@app.get("/registro-proveedor")
def provider_register():
    raw_material = ["Textiles", "Cuero", "Madera", "Piedras", "Metales", "Astas", "Cerámica", "Fibras Vegetales", "Expresión Artística (IND)", "Artesania Ceremonial y de Recoleccion (IND)"]

    return render_template('registro_proveedor.html', tipo_materia = raw_material)

@app.post("/provider")
def create_providers():
    cur, con = db()

    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    company_name = request.json["company_name"]
    document = request.json["document"]
    address = request.json["address"]
    phone_number = request.json["phone_number"]
    city = request.json["city"]
    raw_material = request.json["raw_material"]
    latitude = request.json["latitude"]
    longitude = request.json["longitude"]
    status = request.json["status"]

    result = cur.execute(f"SELECT id, document FROM providers WHERE document = '{document}")
    document_exist = result.fetchone()

    if document_exist is not None:
        return {"error": "El documento ya existe"}

    cur.execute(f"INSERT INTO providers VALUES (null, '{first_name}', '{last_name}', '{company_name}', '{document}', '{address}', '{phone_number}', '{city}', '{raw_material}', '{latitude}', '{longitude}', '{status}')")

    con.commit()

    return {"first_name": first_name}




if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)