import React from 'react';
import './FeedbackControls.scss';

const FeedbackControls = ({ users, selectedUser, sortOrder, onUserChange, onSortChange }) => {
  return (
    <div className="feedback-controls">
      <div className="control-group">
        <label htmlFor="user-select">Filter by User</label>
        <select
          id="user-select"
          value={selectedUser}
          onChange={(e) => onUserChange(e.target.value)}
        >
          <option value="">All Users</option>
          {users.map((user, index) => (
            <option key={index} value={user}>
              {user}
            </option>
          ))}
        </select>
      </div>

      <div className="control-group">
        <label htmlFor="sort-select">Sort by Date</label>
        <select
          id="sort-select"
          value={sortOrder}
          onChange={(e) => onSortChange(e.target.value)}
        >
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
        </select>
      </div>
    </div>
  );
};

export default FeedbackControls;
