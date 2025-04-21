from kafka import KafkaConsumer
import json
from .websocket_server import broadcast_feedback
from .config import Config

def start_kafka_listener():
    try:
        print("🟢 Kafka consumer starting...")
        consumer = KafkaConsumer(
            'feedback-events',
            bootstrap_servers=Config.KAFKA_URL,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        for message in consumer:
            feedback = message.value['feedback']
            print(f"📥 Kafka feedback: {feedback}", flush=True)
            broadcast_feedback(feedback)
    except Exception as e:
        print(f"❌ Kafka consumer error: {e}", flush=True)
