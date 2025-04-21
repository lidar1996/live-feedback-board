from flask import request
import jwt
from flask_socketio import SocketIO
from .config import Config

socketio = SocketIO(cors_allowed_origins="*", async_mode='gevent', logger=True, engineio_logger=True)
connected_users = {}

@socketio.on_error_default
def default_error_handler(e):
    print('❌ SocketIO error:', e, flush=True)

@socketio.on('connect', namespace='/socket.io')
def handle_connect():
    print("Attempting to connect...", dict(request.args), flush=True)
    token = request.args.get('token')
    if not token:
        print("No token provided", flush=True)
        return False
    try:
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get('user_id') or payload.get('username')
        if not user_id:
            print("No valid user identifier in token", flush=True)
            return False

        connected_users[request.sid] = user_id
        print(f"User {user_id} connected!", flush=True)
    except jwt.ExpiredSignatureError:
        print("Token has expired", flush=True)
        return False
    except jwt.InvalidTokenError as e:
        print(f"Invalid token: {e}", flush=True)
        return False

@socketio.on('disconnect')
def handle_disconnect():
    user_id = connected_users.pop(request.sid, None)
    print(f'User {user_id} disconnected', flush=True)

def broadcast_feedback(feedback_data):
    print(f"new_feedback: {feedback_data}", flush=True)
    socketio.emit('new_feedback', feedback_data)
