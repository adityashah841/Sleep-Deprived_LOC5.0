import React from 'react';
import Dashboard from './Dashboard';

function Connector() {
  // Define some example user data
  const userData = {
    username: 'John',
    devices: [
      { id: 1, name: 'Smart Thermostat', type: 'Thermostat', status: 'On', settings: '2kWh', energy: '2kWh' },
      { id: 2, name: 'Smart Air Conditioner', type: 'AC', status: 'On', settings: '3.5kWh', energy: '3.5kWh' },
      { id: 3, name: 'Smart Light Bulbs', type: 'Light Bulb', status: 'Off', settings: '0', energy: '0.06kWh' },
      { id: 4, name: 'Smart Fan', type: 'Fan', status: 'On', settings: '0', energy: '0.09kWh' },
    ],
  };


  return  <Dashboard userData={userData} />
}

export default Connector;
