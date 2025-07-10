from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow other hosts to access

# Dummy users database
users = {
	"operator": "password123",
	"admin": "adminpass"
}

# Dummy login endpoint
@app.route("/login", methods=["POST"])
def login():
	data = request.json
	username = data.get("username")
	password = data.get("password")

	if users.get(username) == password:
    	# In real-world, issue JWT or session
    	return jsonify({"token": f"token-{username}", "message": "Login successful"})
	else:
    	return jsonify({"error": "Invalid credentials"}), 401

# Token validation
@app.route("/validate", methods=["POST"])
def validate():
	token = request.json.get("token")
	if token and token.startswith("token-"):
    	return jsonify({"valid": True})
	return jsonify({"valid": False}), 403

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
