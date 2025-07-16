from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_status():
    return "hello from temp server"




@app.route("/read")
def read_sensor():
    temperature = random.uniform(20.0, 30.0)  # Simulated value
    return jsonify({"temperature": round(temperature, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
