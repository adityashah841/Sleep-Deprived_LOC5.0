import React from 'react';
import './header.css';
import people from '../../assets/people.png';
import ai from '../../assets/energy.png';

const Header = () => {
  return (
    <div className='gpt3__header section__padding' id='home'>
      <div className='gpt3__header-content'>
        <h1 className='gradient__text'>Your OneStop solution for smart energy conservation!</h1>
        <p>Smart energy conservation isn't about doing without, it's about doing more with less.</p>
        <div className='gpt3__header-content__input'>
          <input type='email' placeholder='Enter Email Address for awesome recommendations'/>
          <button type='button'>Get Started</button>
        </div>
        <div className='gpt3__header-content__people'>
          <img src={people} alt='people'/>
          <p>1,600 people requested access a visit in last 24 hours</p>
        </div>
      </div>
      <div className='gpt3__header-image'>
        <img src={ai} alt='ai'/>
      </div>
      
    </div>
  );
}

export default Header;