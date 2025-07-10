from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_status():
    return "hello from pressure server"




@app.route("/read")
def read_sensor():
    pressure = random.uniform(1.0, 5.0)  # Simulated value
    return jsonify({"pressure": round(pressure, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
