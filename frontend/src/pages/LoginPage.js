import React from 'react';
import AuthTabs from '../components/AuthTabs';

function LoginPage({ onLoginSuccess }) {
  return <AuthTabs onLoginSuccess={onLoginSuccess} />;
}

export default LoginPage;
