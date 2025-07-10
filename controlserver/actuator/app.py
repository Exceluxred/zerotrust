from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


state = {"status": "OFF"}


@app.route("/")
def get_index():
    return "hello from actuator server"


@app.route("/status")
def get_status():
    return jsonify(state)

@app.route("/toggle", methods=["POST"])
def toggle():
    state["status"] = "ON" if state["status"] == "OFF" else "OFF"
    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
