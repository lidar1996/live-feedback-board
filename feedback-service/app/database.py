from shared.models import Feedback
from .kafka_producer import send_feedback_event
from flask import current_app
from shared import db

def create_feedback(user_id, content):
    if not user_id or not content:
        current_app.logger.warning(f"user id or content was missing for '{user_id}'.")
        raise ValueError("user_id and content are required")

    feedback = Feedback(user_id=user_id, content=content)

    db.session.add(feedback)
    db.session.commit()
    current_app.logger.warning(f"feedback from '{user_id}' with `{content}` created successfully.")

    send_feedback_event(feedback)

    return feedback


def get_all_feedbacks():
    try:
        feedbacks = Feedback.query.all()
        return feedbacks
    except Exception as e:
        raise ValueError(f"Error fetching feedbacks: {str(e)}")