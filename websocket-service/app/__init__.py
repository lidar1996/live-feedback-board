from flask import Flask
from .websocket_server import socketio
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    socketio.init_app(app)
    return app
