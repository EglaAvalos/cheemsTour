from flask import Flask, request, jsonify
from entities.trip import Trip

app = Flask(__name__)


@app.route("/trips", methods=["GET"])
def trips():
    trips = Trip.get()
    return trips



@app.route('/trip', methods=['POST'])
def save_trip():
    data = request.json
    trip = Trip(name=data['name'], city = data['city'], country=data['country'], latitude=data['latitude'], longitude=data['longitude'])
    id = Trip.save(trip)
    success = id is not None
    return jsonify(success), 201


@app.route('/trip/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    """
    PUT /trip/<trip_id>
    Actualiza un viaje existente.

    Parámetros:
    - trip_id (int): ID del viaje

    JSON esperado:
    {
        "name": "Viaje a Cusco",
        "city": "Cusco",
        "country": "Perú",
        "latitude": -13.5319,
        "longitude": -71.9675
    }

    Respuestas:
    - 200 OK: Actualización exitosa
    - 400 Bad Request: Faltan campos
    - 404 Not Found: No se encontró el viaje
    - 500 Internal Server Error: Error en la base de datos
    """
    data = request.json
    trip = Trip(
        id=trip_id,
        name=data['name'],
        city=data['city'],
        country=data['country'],
        latitude=data['latitude'],
        longitude=data['longitude']
    )
    updated_rows = Trip.update(trip)  


    success = updated_rows > 0
    if updated_rows == 0:
        return jsonify(False), 404
    return jsonify(success), 201


@app.route("/trip/<int:id>", methods=["DELETE"])
def delete_trip(id):
    deleted = Trip.delete(id)
    success = deleted > 0
    return jsonify(success), 201



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
