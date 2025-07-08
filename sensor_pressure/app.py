from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/read")
def read_sensor():
    pressure = random.uniform(1.0, 5.0)  # Simulated value
    return jsonify({"pressure": round(pressure, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
