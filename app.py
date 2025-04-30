from flask import Flask
from entities.trip import Trip

app = Flask(__name__)

@app.route('/trips', methods=['GET'])
def trips():
    trips = Trip.get()
    return trips



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)