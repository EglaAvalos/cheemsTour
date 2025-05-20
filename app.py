from flask import Flask, request, jsonify
from entities.trip import Trip

app = Flask(__name__)

@app.route('/trips', methods=['GET'])
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

@app.route('/trip', methods=['PUT'])
def update_trip():
     data = request.json
     trip= Trip(name=data['name'], city=data['city'],country=data['country'],  latitude=data['latitude'], longitude=data['longitude'])
     id = Trip.save(trip)
     success = id is not None
     return jsonify(success), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)