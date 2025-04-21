import React, { useEffect, useState } from 'react';
import FeedbackBoard from '../components/FeedbackBoard';
import FeedbackForm from '../components/FeedbackForm';
import FeedbackControls from '../components/FeedbackControls';
import { getFeedbacks, sendFeedback } from '../api/api';
import { useNavigate } from 'react-router-dom';
import useSocket from '../hooks/useSocket';
import './FeedbackPage.scss';

const FeedbackPage = () => {
  const [feedbacks, setFeedbacks] = useState([]);
  const [error, setError] = useState('');
  const [selectedUser, setSelectedUser] = useState('');
  const [sortOrder, setSortOrder] = useState('newest');
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  const socketUrl = process.env.REACT_APP_FEEDBACK_WS_URL;

  useEffect(() => {
    if (!token) {
      navigate('/login');
    }
  }, [navigate, token]);

  useEffect(() => {
    const fetchFeedbacks = async () => {
      try {
        const feedbacks = await getFeedbacks();
        setFeedbacks(feedbacks);
      } catch (err) {
        setError('Failed to fetch feedbacks');
      }
    };

    fetchFeedbacks();
  }, []);

  const handleFeedbackSubmit = async (message) => {
    try {
      await sendFeedback(message);
    } catch (err) {
      setError('Failed to send feedback');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  const onMessage = (message) => {
    setFeedbacks((prevFeedbacks) => [...prevFeedbacks, message]);
  };

  useSocket(socketUrl, token, onMessage);

  const uniqueUsers = [...new Set(feedbacks.map(f => f.user_name).filter(Boolean))];

  const filteredAndSortedFeedbacks = feedbacks
    .filter(fb => !selectedUser || fb.user_name === selectedUser)
    .sort((a, b) => {
      const dateA = new Date(a.created_at);
      const dateB = new Date(b.created_at);
      return sortOrder === 'newest' ? dateB - dateA : dateA - dateB;
    });

  return (
    <div className="feedback-page">
      <button className="logout" onClick={handleLogout}>Logout</button>
      <h1>Feedbacks Board</h1>
      {error && <p className="error">{error}</p>}

      <FeedbackControls
        users={uniqueUsers}
        selectedUser={selectedUser}
        sortOrder={sortOrder}
        onUserChange={setSelectedUser}
        onSortChange={setSortOrder}
      />

      <FeedbackBoard feedbacks={filteredAndSortedFeedbacks} />
      <FeedbackForm onSubmit={handleFeedbackSubmit} />
    </div>
  );
};

export default FeedbackPage;
