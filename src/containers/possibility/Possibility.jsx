import React from 'react';
import possibilityImage from '../../assets/possibility.png';
import './possibility.css';

const Possibility = () => {
  return (
    <div className="gpt3__possibility section__padding" id="possibility">
    <div className="gpt3__possibility-image">
      <img src={possibilityImage} alt="possibility" />
    </div>
    <div className="gpt3__possibility-content">
      <h4>Request Early Access to Get Started</h4>
      <h1 className="gradient__text">The possibilities are <br /> beyond your imagination</h1>
      <p>Conserving energy is a win-win situation for everyone, it saves the planet and benefits your wallet too.Remember, every time you switch off a light or unplug an appliance, you are taking a step towards a more sustainable future.</p>
      <h4>Request Early Access to Get Started</h4>
    </div>
  </div>
  )
}

export default Possibility