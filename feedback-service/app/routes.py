from flask import Blueprint, request, jsonify
from .database import create_feedback, get_all_feedbacks
from .config import Config
import requests
from functools import wraps

feedback_bp = Blueprint('feedback', __name__)

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]
        try:
            response = requests.post(Config.AUTH_SERVICE_URL, json={"token": token})
            if response.status_code != 200:
                return jsonify({"error": "Invalid or expired token"}), 401
            request.user_id = response.json().get("user_id")
        except Exception as e:
            return jsonify({"error": str(e) + " Auth service unavailable"}), 500

        return f(*args, **kwargs)
    return decorated_function

@feedback_bp.route('/feedback', methods=['POST'])
@jwt_required
def create():
    data = request.get_json()
    try:
        feedback = create_feedback(request.user_id, data)
        if feedback:
            return jsonify({
                'message': 'Feedback created successfully',
                'feedback': feedback.to_dict()
            }), 201
        return jsonify({"message": "Invalid params"}), 401
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

@feedback_bp.route('/feedbacks', methods=['GET'])
@jwt_required
def get_feedbacks():
    try:
        feedbacks = get_all_feedbacks()
        return jsonify([feedback.to_dict() for feedback in feedbacks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
