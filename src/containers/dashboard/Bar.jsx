import React, { useState } from 'react';
import './bar.css';

const Bar = () => {
  const [progress, setProgress] = useState(0);

  const handleClick = () => {
    if (progress < 100) {
      setProgress(progress + 10);
    }
  };

  const getColor = () => {
    const hue = ((100 - progress) / 100) * 120;
    return `hsl(${hue}, 100%, 50%)`;
  };

  return (
    <div className="progress-circle-container">
      <svg viewBox="0 0 36 36">
        <path
          className="progress-circle-bg"
          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
        />
        <path
          className="progress-circle"
          stroke={getColor()}
          strokeWidth="2"
          fill="none"
          strokeLinecap="round"
          strokeDasharray={`${progress}, 100`}
          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
          onClick={handleClick}
        />
      </svg>
      <div className="progress-circle-text">{`${progress}%`}</div>
    </div>
  );
};

export default Bar;