import React from 'react';
import '../App.css';
import './client.css';
import {Link} from 'react-router-dom';


function LoginPage() {
  return (
    
    <div className ="bg">
        
    <div className ="login">
        <h1> Login Page </h1>
        <div className ="form-box">
            <input type ="text" name = "username/email" placeholder="Enter Email/Username" onfocus="this.placeholder = ''"
            onblur="this.placeholder = 'Enter Email/Username'" required />

            <input type="password" name="password" placeholder="Enter Password" onfocus="this.placeholder = ''"
            onblur="this.placeholder = 'Enter Password'"required />

            <div className= "bottomright">
                {/*<a href = "forgotPass.html"> Forgot Password?</a>*/}
                <Link className="bottomright" to = "/forgot">
                    Forgot Password?
                </Link>
            </div>

            <div id="btn">
                <div className="button-box">
                    <button type="submit" className="toggle-btn">Login</button>
                    <button type="submit" className="toggle-btn">Register</button>
                    
                </div> 
            </div>
            
        </div>
    </div>
</div>
  );
}

export default LoginPage;
