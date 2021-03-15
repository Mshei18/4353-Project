import React from 'react';
import '../App.css';
import './client.css';
import {Link} from 'react-router-dom';

function NewPassword() {
  return (
    <div > 
        
        <div className ="login">
            <h1> New Password Page </h1>

            <div className ="form-box">
                <input type ="password" name = "newPassword" placeholder="Enter New Password" onfocus="this.placeholder = ''"
                onblur="this.placeholder = 'Enter New Password'" required />

                <input type ="password" name = "rnewPassword" placeholder="Renter New Password" onfocus="this.placeholder = ''"
                onblur="this.placeholder = 'Renter New Password'" required />

                <div className="button-box">
                    <div className="NPcenter-button">
                        {/*<button type="submit" className="toggle-btn"><a href="passReset.html">Submit</a></button>*/}
                        <Link className="toggle-btn" to = "/passwordreset">
                            Submit
                        </Link>
                    </div>
                </div>

            </div>
            
            


        </div>

        
    </div>
  );
}

export default NewPassword;
