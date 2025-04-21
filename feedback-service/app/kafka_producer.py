from kafka import KafkaProducer
import json
from .config import Config

producer = KafkaProducer(
    bootstrap_servers=[Config.KAFKA_URL],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_feedback_event(feedback):
    event_data = {
        'event': 'feedback.created',
        'feedback': feedback.to_dict()
    }
    print("send message", event_data)
    producer.send('feedback-events', value=event_data)
