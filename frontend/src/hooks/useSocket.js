import { useEffect, useRef } from 'react';
import { io } from 'socket.io-client';

const useSocket = (url, token, onMessage) => {
  const socketRef = useRef(null);

  useEffect(() => {
    if (!url || !token) return;

    const socket = io(url, {
      query: { token },
      transports: ['websocket'],
    });

    socketRef.current = socket;

    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('disconnect', () => {
      console.log('Disconnected from server');
    });

    socket.on('new_feedback', (data) => {
      onMessage(data);
    });

    return () => {
      socket.disconnect();
    };
  }, [url, token, onMessage]);

  return socketRef.current;
};

export default useSocket;
