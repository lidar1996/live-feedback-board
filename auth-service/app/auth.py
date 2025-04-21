import jwt
import redis
from datetime import datetime, timedelta
from .database import get_user_by_username
from .config import Config
from flask import current_app
from shared import db
from shared.models import User

redis_client = redis.Redis.from_url(Config.REDIS_URL)

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(minutes=Config.JWT_EXPIRATION_DELTA)
    }

    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm="HS256")
    redis_client.setex(f"session:{username}", timedelta(minutes=Config.JWT_EXPIRATION_DELTA), token)

    return token


def login(username, password):
    user = get_user_by_username(username)
    if not user:
        current_app.logger.warning(f"Login failed: user '{username}' not found.")
        raise ValueError("Invalid username or password")
    if not user.check_password(password):
        current_app.logger.warning(f"Login failed: wrong password for user '{username}'.")
        raise ValueError("Invalid username or password")

    return generate_token(username)


def register(username, password):
    if get_user_by_username(username):
        current_app.logger.warning(f"Registration failed: user '{username}' already exists.")
        raise ValueError("User already exists")

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    current_app.logger.info(f"User '{username}' registered successfully.")
    return generate_token(username)


def validate_token(token):
    try:
        decoded = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
        username = decoded.get('username')
        if redis_client.exists(f"session:{username}") and redis_client.get(f"session:{username}").decode("utf-8") == token:
            user = get_user_by_username(username)
            return user.id
        else:
            return None
    except jwt.ExpiredSignatureError:
        current_app.logger.warning(f"JWT token expired")
        return None
    except jwt.InvalidTokenError:
        current_app.logger.warning(f"Invalid JWT token")
        return None

def logout(token):
    redis_client.delete(token)