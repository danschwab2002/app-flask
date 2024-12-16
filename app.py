from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return "¡Hola! Bienvenido a la aplicación de gestión de reservas."

# Ruta para crear una reserva (simulación)
@app.route("/reservas", methods=["POST"])
def agregar_reserva():
    data = request.json
    nombre = data.get("nombre")
    cantidad_personas = data.get("cantidad_personas")
    fecha = data.get("fecha")
    horario = data.get("horario")
    return jsonify({
        "message": "Reserva creada exitosamente",
        "reserva": {
            "nombre": nombre,
            "cantidad_personas": cantidad_personas,
            "fecha": fecha,
            "horario": horario
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
