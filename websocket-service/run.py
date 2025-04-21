from app import create_app
from app.kafka_consumer import start_kafka_listener
import threading
from app.websocket_server import socketio

app = create_app()

threading.Thread(target=start_kafka_listener, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app, port=5003, debug=True)
