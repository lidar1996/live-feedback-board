from flask import Blueprint, request, jsonify
from .auth import login, register, validate_token, logout

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    try:
        token = login(data.get("username"), data.get("password"))
        if token:
            return jsonify({"token": token}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout_route():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token required"}), 401

    token = token.replace("Bearer ", "")
    logout(token)
    return jsonify({"message": "Logged out successfully"})

@auth_bp.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()
    try:
        username = data.get("username")
        password = data.get("password")
        token = register(username, password)
        if token:
            return jsonify({"token": token}), 201
        return jsonify({"message": "Username already exists"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route('/verify-token', methods=['POST'])
def verify_token():
    token = request.get_json()["token"]
    if not token:
        return jsonify({"message": "Missing token"}), 401
    user_id = validate_token(token)
    if user_id is not None:
        return jsonify({"user_id": user_id}), 200
    else:
        return jsonify({"message": "Invalid token"}), 401
