from flask import Flask, request, jsonify, Response
import json, webbrowser
import uuid
import htmlstyles

PASSWORD = "cefono"

app = Flask(__name__)
class Database:
    def __init__(self, filename="data.jtxt"):
        self.filename = filename
        self.data = {"profesionales": [], "pacientes": [], "turnos": []}  # Default structure
        print("Database initialized")

    def readfile(self):
        try:
            with open(self.filename, "r") as DBFile:
                self.data = json.load(DBFile)
                print("Database loaded from file")
        except FileNotFoundError:
            print("File not found, initializing with default database structure")
        except json.JSONDecodeError:
            print("Error decoding JSON, initializing with default database structure")

    def writefile(self):
        with open(self.filename, "w") as DBFile:
            json.dump(self.data, DBFile, indent=4)
            print("Database written to file")

    def __str__(self):
        # Return a string representation of the database
        return json.dumps(self.data, indent=4)

DB = Database()
DB.readfile()  # Load data from the file
print(DB.data["pacientes"])

def check_auth(password):
    return password == PASSWORD

def authenticate():
    return Response(
        'Unauthorized access. Please log in.', 401,
        {'WWW-Authenticate': 'Basic realm="Password Required"'}
    )

@app.before_request
def restrict_access():
    auth = request.authorization
    # Check if the password is provided and valid
    if not auth or not check_auth(auth.password):
        return authenticate()

index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cefono</title>
    <style>%!STYLE!%</style>
</head>
<body>
    <h1>Registrar profesional</h1>
    <form action="http://127.0.0.1:2336/register" method="POST">
        <label for="categoria">Tipo:</label><br>
        <select id="categoria" name="categoria" required>
            <option value="">--Selecciona una categoría--</option>
            <option value="fonoaudiologia">Fonoaudiología</option>
            <option value="psicololgia">Psicología</option>
            <option value="psicopedagogia">Psicopedagogía</option>
            <option value="terapiaocupacional">Terapia Ocupacional</option>
            <option value="nutricion">Nutrición</option>
            <option value="kinesiologia">Kinesiología</option>
        </select><br><br>

        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" required><br><br>
        
        <label for="whatsapp">Número de teléfono:</label><br>
        <input type="tel" id="whatsapp" name="whatsapp" required><br><br>
        
        <input type="hidden" id="clase" name="clase" value="profesional">
        <button type="submit">Submit</button>
    </form>

    <h1>Registrar paciente</h1>
    <form action="http://127.0.0.1:2336/register" method="POST">

        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" required><br><br>
        <label for="apellido">Apellido:</label><br>
        <input type="text" id="apellido" name="apellido" required><br><br>

        <label for="whatsapp">Número de teléfono:</label><br>
        <input type="tel" id="whatsapp" name="whatsapp" required><br><br>
        
        <label for="obrasocial">Obra social:</label><br>
        <select id="obrasocial" name="obrasocial" required>
            <option value="">--Obra social--</option>
            <option value="apres">Apres</option>
            <option value="osde">OSDE</option>
            <option value="ioma">IOMA</option>
            <option value="ospoce">OSPOCE</option>
            <option value="pami">PAMI</option>
            <option value="other">Particular</option>
        </select><br><br>

        <input type="hidden" id="clase" name="clase" value="paciente">
        <button type="submit">Submit</button>
    </form>

    <h1>Registrar turno</h1>
    <form action="http://127.0.0.1:2336/register" method="POST">

        <label for="profesional">Profesional:</label><br>
        <select id="profesional" name="profesional" required>
            %!PROFESIONAL!%
        </select><br><br>

        <label for="paciente">Paciente:</label><br>
        <select id="paciente" name="paciente" required>
            %!PACIENTE!%
        </select><br><br>

        <label for="fecha">Fecha:</label><br>
        <input type="datetime-local" id="fecha" name="fecha" required><br><br>
        
        <input type="hidden" id="unix_fecha" name="unix_fecha">
    
        <input type="hidden" id="clase" name="clase" value="turno">
    
        <button type="submit">Submit</button>
    </form>
    <h1>BASE DE DATOS</h1>
    %!DATABASE!%
"""

gptstylesheet = htmlstyles.gpt4

claudestylesheet = htmlstyles.claude

@app.route('/', methods=['GET'])
def index():
    global DB
    data = """<h1>Datos</h1>
    """

    lista_de_profesionales = '<option value="">--Selecciona una profesional--</option>'
    for profesional in DB.data['profesionales']:
        data = data + "<h3>Profesional</h3><ul><li>" + profesional["nombre"] + "</li>" + "<li>" + profesional["whatsapp"] + "</li>" + "<li>" + profesional["categoria"] + "</li>" + "</ul>"
        lista_de_profesionales = lista_de_profesionales + f"""<option value="{profesional["identificador"]}">{profesional["nombre"]}</option>"""
    
    lista_de_pacientes = '<option value="">--Selecciona un paciente--</option>'
    for paciente in DB.data['pacientes']:
        data = data + "<h3>Paciente</h3><ul><li>" + paciente["apellido"] + ", " + paciente["nombre"] + "</li>" + "<li>" + paciente["whatsapp"] + "</li>" + "<li>" + paciente["obra_social"] + "</li>" + "</ul>"
        lista_de_pacientes = lista_de_pacientes + f"""<option value="{paciente["identificador"]}">{paciente["nombre"] + " " + paciente["apellido"]}</option>"""

    for turno in DB.data['turnos']:
        for paciente in DB.data['pacientes']:
            if paciente['identificador'] == turno['paciente_id']:
                paciente_nombre = paciente['nombre'] + ", " + paciente['apellido']
        for profesional in DB.data['profesionales']:
            if profesional['identificador'] == turno['profesional_id']:
                profesional_nombre = profesional['nombre']
        data = data + "<h3>Turno</h3><ul><li>" + profesional_nombre + "</li>" + "<li>" + paciente_nombre + "</li>" + "<li>" + turno['fecha'] + "</li></ul>"

    return index_html.replace("%!DATABASE!%", json.dumps(DB.data)).replace("%!PROFESIONAL!%", lista_de_profesionales).replace("%!PACIENTE!%", lista_de_pacientes).replace("%!STYLE!%", claudestylesheet) + data + "\n</body>\n</html>"

@app.route('/register', methods=['POST'])
def register():
    global DB
    clase = request.form.get('clase')
    if clase == "profesional":
        # registrar profesional
        nombre = request.form.get('nombre')
        whatsapp = request.form.get('whatsapp')
        categoria = request.form.get('categoria')
        profesional = {
            "nombre": nombre.strip().title(),
            "whatsapp": whatsapp,
            "categoria": categoria,
            "identificador": str(uuid.uuid4())
        }
        DB.data['profesionales'].append(profesional)
        print(DB.data)

    elif clase == "paciente":
        # registrar paciente
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        obra_social = request.form.get('obrasocial')
        whatsapp = request.form.get('whatsapp')
        paciente = {
            "nombre": nombre.strip().title(),
            "apellido": apellido.strip().title(),
            "obra_social": obra_social,
            "whatsapp": whatsapp,
            "identificador": str(uuid.uuid4())
        }
        DB.data['pacientes'].append(paciente)
        print(DB.data)

    elif clase == "turno":
        paciente_uuid = request.form.get('paciente')  # UUID
        profesional_uuid = request.form.get('profesional')  # UUID
        fecha = request.form.get('fecha')

        if not paciente_uuid or not profesional_uuid or not fecha:
            return jsonify({"error": "Faltan cosas"}), 400

        paciente_object = next((p for p in DB.data["pacientes"] if p["identificador"] == paciente_uuid), None)
        profesional_object = next((p for p in DB.data["profesionales"] if p["identificador"] == profesional_uuid), None)

        if not paciente_object:
            return jsonify({"error": "Paciente no registrado"}), 404
        if not profesional_object:
            return jsonify({"error": "Profesional no registrado"}), 404

        turno = {
            "profesional_id": profesional_uuid,
            "paciente_id": paciente_uuid,
            "fecha": fecha
        }
        DB.data["turnos"].append(turno)
    else:
        pass

    DB.writefile()

    return """<!DOCTYPE html><html lang="en"><head><meta http-equiv="refresh" content="0; url=/" /><title>Redirecting...</title></head><body><p>If you are not redirected automatically, <a href="/">click here</a>.</p></body></html>"""

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:2336")
    app.run(debug=False, host='0.0.0.0', port=2336)