from flask import Flask
from flask_cors import CORS
from .routes import feedback_bp
from shared import db
import logging

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')
    app.config.from_object('shared.config.Config')

    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        app.logger.info("✅ Database tables checked/created.")

    app.register_blueprint(feedback_bp)

    return app
