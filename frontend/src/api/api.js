const BASE_URL = process.env.REACT_APP_AUTH_URL;

export async function loginOrRegister(type, username, password) {
    const endpoint = `${BASE_URL}/${type}`;
  
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });
    const data = await res.json();
    if (!res.ok) {
      return { error: data.error || 'Something went wrong' };
    }
    return { token: data.token };
  }

  export async function sendFeedback(feedbackData) {
    const token = localStorage.getItem('token');
    const response = await fetch(`${process.env.REACT_APP_FEEDBACK_URL}/feedback`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(feedbackData),
    });
  
    if (!response.ok) {
      throw new Error('Failed to send feedback');
    }
  
    const data = await response.json();
    return data;
  }

  export async function getFeedbacks() {
    const token = localStorage.getItem('token');
    const response = await fetch(`${process.env.REACT_APP_FEEDBACK_URL}/feedbacks`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });
  
    if (!response.ok) {
      throw new Error('Failed to fetch feedbacks');
    }
  
    const data = await response.json();
    return data;
  }
