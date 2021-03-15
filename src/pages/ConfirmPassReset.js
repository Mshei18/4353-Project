import React from 'react';
import '../App.css';
import './client.css';
import {Link} from 'react-router-dom';

function ConfirmPassReset() {
  return (
    <div > 
        
        <div className ="login">
            
            
            <h2> Password has been Reset!</h2>
            
            
            <div >
                <Link className="toggle-btn" to = "/login">
                    Return to Login
                </Link>
            </div>
            

        </div>
    </div>
  );
}

export default ConfirmPassReset;
