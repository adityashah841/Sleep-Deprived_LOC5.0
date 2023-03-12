import React from 'react';
import Blog from '../blog/Blog';

import './dashboardB.css';
import bulb from '../../assets/bulb.png'

function DashboardB(props) {
  const { username, devices } = props.userData;

  return (
    
    <div className="user-homepage1">
        <div className="header1">
            <h1 className='text_color1'>Welcome back, {username}!</h1>
            <p className='p_text1'>Here are your connected devices:</p>
            <div className='device_list_box1'>
                <ul className='device_list1'>
                {devices.map((device) => (
                    <li key={device.id}>{device.name}</li>
                    ))}
                </ul>
            </div>
            <img className='dash_img1' src={bulb} alt='ai'/>
                <div className='power_btn'>
                    <button type="submit" className='low' >Low Consumption Mode</button>
                    <button type="submit" className='med' >Medium Consumption Mode</button>
                    <button type="submit" className='high' >High Consumption Mode</button>
                </div>
            <hr></hr>
    
        </div>
        <div className="devices1">
            <h2>My Devices</h2>
            <div className="device-list1">
            {devices.map((device) => (
                <div key={device.id} className="device-card1">
                <div className="device-card-header1">
                    <h3>{device.name}</h3>
                    <p>{device.type}</p>
                </div>
                <div className="device-card-body1">
                    {/* This is where you would display information about the device, such as its status, settings, etc. */}
                    <p>Status: {device.status}</p>
                    <p>Settings: {device.settings}</p>
                    <p>Power Consumption: {device.energy}</p>
                </div>
                </div>
            ))}
            </div>
            <hr></hr>
        </div>
        <Blog/>
    </div> 
    
  );
}

export default DashboardB;