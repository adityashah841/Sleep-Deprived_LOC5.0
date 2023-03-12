import React from 'react';
import Blog from '../blog/Blog';

import './dashboard.css';
import ai from '../../assets/ai.png'
import Bar from './Bar';
import axios from 'axios'

function Dashboard(props) {
  const { username, devices } = props.userData;
  axios.get(
    "https://2b2e-2402-3a80-138e-3664-fc45-ab4c-9faf-6608.in.ngrok.io/ml/dashboard/"
  ).then((response) => {
    const data = response
    console.log(data)
  })
  return (
    
    <div className="user-homepage">
        <div className="header">
            <h1 className='text_color'>Welcome back, {username}!</h1>
            <p className='p_text'>Here are your connected devices:</p>
            <div className='device_list_box'>
                <ul className='device_list'>
                {devices.map((device) => (
                    <li key={device.id}>{device.name}</li>
                    ))}
                </ul>
            </div>
            <img className='dash_img' src={ai} alt='ai'/>
            {/* <Bar/> */}
            <hr></hr>
    
        </div>
        <div className="devices">
            <h2>My Devices</h2>
            <div className="device-list">
            {devices.map((device) => (
                <div key={device.id} className="device-card">
                <div className="device-card-header">
                    <h3>{device.name}</h3>
                    <p>{device.type}</p>
                </div>
                <div className="device-card-body">
                    {/* This is where you would display information about the device, such as its status, settings, etc. */}
                    <p>Status: {device.status}</p>
                    <p>Power Consumption: {device.settings}</p>
                    <p>Power Rating: {device.energy}</p>
                </div>
                </div>
            ))}
            </div>
            <button type="submit">Use Geyser</button>
            <hr></hr>
        </div>
        <Blog/>
        
    </div> 
    
  );
}

export default Dashboard;


