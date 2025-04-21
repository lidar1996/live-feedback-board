import os

class Config:
    KAFKA_URL = os.getenv('KAFKA_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET')
    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL')