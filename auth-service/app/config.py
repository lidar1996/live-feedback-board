import os

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET')
    JWT_EXPIRATION_DELTA = int(os.getenv('JWT_EXP_MINUTES', 60))
    REDIS_URL = os.getenv('REDIS_URL')
