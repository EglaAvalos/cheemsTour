from flask import Flask, request, jsonify
from entities.trip import Trip

app = Flask(__name__)

@app.route('/trips', methods=['GET'])
def get_trips():
    trips = Trip.get()
    return jsonify(trips)

@app.route('/trips/<int:id>', methods=['GET'])
def get_trip(id):
    trip = Trip.get_by_id(id)
    if trip:
        return jsonify(trip)
    return jsonify({'message': 'Trip not found'}), 404

@app.route('/trips', methods=['POST'])
def create_trip():
    data = request.get_json()
    name = data.get('name')
    city = data.get('city')
    country = data.get('country')
    result = Trip.create(name, city, country)
    return jsonify(result)

@app.route('/trips/<int:id>', methods=['PUT'])
def update_trip(id):
    data = request.get_json()
    name = data.get('name')
    city = data.get('city')
    country = data.get('country')
    result = Trip.update(id, name, city, country)
    return jsonify(result)

@app.route('/trips/<int:id>', methods=['DELETE'])
def delete_trip(id):
    result = Trip.delete(id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
