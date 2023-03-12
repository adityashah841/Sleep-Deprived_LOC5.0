import React from 'react';
import DashboardB from './DashboardB';

function ConnectorB() {
  // Define some example user data
  const userData = {
    username: 'John',
    devices: [
      { id: 1, name: 'Smart Air Conditioner 1', type: 'AC', status: 'On', settings: '19 degrees', energy: '3.2kWh' },
      { id: 2, name: 'Smart Air Conditioner 2', type: 'AC', status: 'On', settings: '21 degrees', energy: '3.5kWh' },
      { id: 3, name: 'Smart Air Conditioner 3', type: 'AC', status: 'Off', settings: '24 degrees', energy: '3.6kWh' },
      { id: 4, name: 'Smart Air Conditioner 4', type: 'AC', status: 'On', settings: '22 degrees', energy: '3.9kWh' },
    ],
  };

  return  <DashboardB userData={userData} />
}

export default ConnectorB;