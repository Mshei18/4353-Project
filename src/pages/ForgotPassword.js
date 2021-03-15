import React from 'react';
import '../App.css';
import './client.css';
import {Link} from 'react-router-dom';

function ClientProfile() {
  return (
    <div > 
        
        <div className ="login">
            <h1> Forgot Password Page </h1>
            
            <div className ="form-box">
                <input type ="text" name = "username/email" placeholder="Enter Email/Username" onfocus="this.placeholder = ''"
                onblur="this.placeholder = 'Enter Email/Username'" required />
                
                <div className="button-box">
                    <div className="center-button">
                        {/*<button type="submit" className="toggle-btn"><a href="newPass.html">Next</a></button>*/}
                        <Link className="toggle-btn" to = "/setnewpassword">
                            Next
                        </Link>
                </div>
            </div>
        </div>


        </div>

        
    </div>
  );
}

export default ClientProfile;
