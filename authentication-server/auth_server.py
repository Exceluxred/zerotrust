from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)  # Allow other hosts to access
app.config['SECRET_KEY'] = 'your-very-secure-secret-key-here'  # In production, use environment variables

# Enhanced users database with roles
users = {
    "operator": {
        "password": "password123",  # In production, store hashed passwords
        "role": "operator",
        "permissions": ["read_sensors"]
    },
    "admin": {
        "password": "adminpass",
        "role": "admin",
        "permissions": ["read_sensors", "toggle_actuator", "view_logs", "manage_users"]
    }
}

# JWT token generation
def generate_token(username):
    payload = {
        'username': username,
        'role': users[username]['role'],
        'permissions': users[username]['permissions'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expires in 30 minutes
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

#Token required decorator
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
            current_user = {
                'username': data['username'],
                'role': data['role'],
                'permissions': data['permissions']
            }
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
            
        return f(current_user, *args, **kwargs)
        
    return decorated


# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if username not in users or users[username]['password'] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(username)
    
    # Log the login attempt (in a real system, store this in a database)
    print(f"Login successful for user: {username}")
    
    return jsonify({
        "token": token,
        "user": {
            "username": username,
            "role": users[username]['role'],
            "permissions": users[username]['permissions']
        },
        "message": "Login successful"
    })

# Token validation endpoint
@app.route("/validate", methods=["POST"])
@token_required
def validate(current_user):
    return jsonify({
        "valid": True,
        "user": {
            "username": current_user['username'],
            "role": current_user['role'],
            "permissions": current_user['permissions']
        }
    })

# Get current user info
@app.route("/me", methods=["GET"])
@token_required
def get_current_user(current_user):
    return jsonify(current_user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#====================================================================================================

# In actuator/app.py - fix the token_required decorator
