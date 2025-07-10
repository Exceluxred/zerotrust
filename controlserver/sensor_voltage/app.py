from flask import Flask, jsonify
import random

from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route("/")
def get_status():
    return "hello from voltage server"


@app.route("/read")
def read_sensor():
    voltage = random.uniform(110.0, 240.0)  # Simulated value
    return jsonify({"voltage": round(voltage, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
