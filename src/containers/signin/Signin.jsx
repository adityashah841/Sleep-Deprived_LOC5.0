import './signin.css';
import React, { useState } from "react";
import axios from 'axios';
import { useEffect} from 'react'


const Signin = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [verify, setVerify] = useState(false);

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    
    event.preventDefault();
    console.log(`Email: ${email}, Password: ${password}`);
    axios.post("https://2b2e-2402-3a80-138e-3664-fc45-ab4c-9faf-6608.in.ngrok.io/api/login/", {
      email: email,
      password: password
    })
    .then((response) => {
      console.log(response);
      if (response.data){
        window.location.href = "/dashboard"
      }
      else{
        alert("no user found")
      }
    })
  };


  return (
    <div className='gradient__bg1'>
      <div className="login-wrapper">
        <h2 className='slide-top'>Login</h2>
        <form className='signinForm' onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={handleEmailChange}
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={handlePasswordChange}
            />
          </div>
          <button type="submit" className='signin_btn'>Submit</button>
        </form>
      </div>
    </div>
  );
};





export default Signin