import os

class Config:
    KAFKA_URL = os.getenv('KAFKA_URL')
    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL')