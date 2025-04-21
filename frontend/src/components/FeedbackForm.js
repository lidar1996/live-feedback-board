import React, { useState } from 'react';
import './FeedbackForm.scss';

const FeedbackForm = ({ onSubmit }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSubmit(message);
      setMessage('');
    }
  };

  return (
    <form className="feedback-form" onSubmit={handleSubmit}>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Write a feedback...."
      />
      <button type="submit">Send</button>
    </form>
  );
};

export default FeedbackForm;
