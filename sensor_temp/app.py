from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/read")
def read_sensor():
    temperature = random.uniform(20.0, 30.0)  # Simulated value
    return jsonify({"temperature": round(temperature, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
