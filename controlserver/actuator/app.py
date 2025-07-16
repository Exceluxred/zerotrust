from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
from functools import wraps

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-very-secure-secret-key-here'  # Must match auth server

state = {"status": "OFF"}

# Token required decorator for actuator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            if 'toggle_actuator' not in data['permissions']:
                return jsonify({'message': 'Insufficient permissions!'}), 403

            current_user = {
                'username': data['username'],
                'role': data['role'],
                'permissions': data['permissions']
            }

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route("/")
def get_index():
    return "hello from actuator server"

@app.route("/status")
def get_status():
    return jsonify(state)

@app.route("/toggle", methods=["POST"])
@token_required
def toggle(current_user):
    state["status"] = "ON" if state["status"] == "OFF" else "OFF"
    print(f"Actuator toggled to {state['status']} by {current_user['username']}")
    return jsonify(state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
