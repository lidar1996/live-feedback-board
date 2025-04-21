import React, { useState } from 'react';
import { loginOrRegister } from '../api/api';
import './AuthTabs.scss';
import { useNavigate } from 'react-router-dom';

function AuthTabs() {
  const [activeTab, setActiveTab] = useState('login');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleTabChange = (tab) => {
    setActiveTab(tab);
    setUsername('');
    setPassword('');
    setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { token, error } = await loginOrRegister(activeTab, username, password);
    if (error) {
      setError(error);
      return;
    }
    localStorage.setItem('token', token);
    navigate('/feedback');
  };

  return (
    <div className="auth-container">
      <div className="tabs">
        <button
          className={activeTab === 'login' ? 'tab active' : 'tab'}
          onClick={() => handleTabChange('login')}
        >
          Login
        </button>
        <button
          className={activeTab === 'register' ? 'tab active' : 'tab'}
          onClick={() => handleTabChange('register')}
        >
          Register
        </button>
      </div>

      <form onSubmit={handleSubmit} className="auth-form">
        <input
          type="text"
          placeholder="Username"
          value={username}
          required
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          required
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && <p className="error">{error}</p>}
        <button type="submit">
          {activeTab === 'login' ? 'Login' : 'Register'}
        </button>
      </form>
    </div>
  );
}

export default AuthTabs;
