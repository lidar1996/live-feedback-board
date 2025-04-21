import React from 'react';
import './FeedbackBoard.scss';

const FeedbackBoard = ({ feedbacks }) => {
  if (feedbacks.length === 0) return (
    <p>No feedbacks yet.</p>
  );
  return (
    <div className="feedback-board">
      {feedbacks.map((fb, i) => (
        <div key={i} className="feedback-item">
              <strong>{fb.user_name}</strong>: {fb.content}
              <br />
              <small>{new Date(fb.created_at).toLocaleString()}</small>
        </div>
      ))}
    </div>
  );
};

export default FeedbackBoard;
