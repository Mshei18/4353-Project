import React from 'react';
import '../App.css';
import './client.css';

function ClientProfile() {
  return (
    <div > {/*className = "bg-image"*/}
        
        <div className ="login">
        <h1> Client Profile Page </h1>
            <form>
                <label htmlFor="fullName">Full Name</label> <br/>
                <input type="text" id="fullName" name="profile" maxlength = "50" required /> <br/>
                
                
                <label htmlFor="address1">Address 1</label> <br/>
                <input type="text" id="address1" name="profile" maxlength = "100" required /> <br/>
                
                <label htmlFor="address2">Address 2</label> <br/>
                <input type="text" id="address2" name="profile" maxlength = "100" /> <br/>
                
                <label htmlFor="city">City</label> <br/>
                <input type="text" id="city" name="profile" maxlength = "100" required /> <br/>

                <label htmlFor="state">State</label>  <br/>
                <select name="state" id="state"> 
                    <option value="" selected="selected">Select a State</option>
                    <option value="AL">Alabama</option>
                    <option value="AK">Alaska</option>
                    <option value="AZ">Arizona</option>
                    <option value="AR">Arkansas</option>
                    <option value="CA">California</option>
                    <option value="CO">Colorado</option>
                    <option value="CT">Connecticut</option>
                    <option value="DE">Delaware</option>
                    <option value="DC">District Of Columbia</option>
                    <option value="FL">Florida</option>
                    <option value="GA">Georgia</option>
                    <option value="HI">Hawaii</option>
                    <option value="ID">Idaho</option>
                    <option value="IL">Illinois</option>
                    <option value="IN">Indiana</option>
                    <option value="IA">Iowa</option>
                    <option value="KS">Kansas</option>
                    <option value="KY">Kentucky</option>
                    <option value="LA">Louisiana</option>
                    <option value="ME">Maine</option>
                    <option value="MD">Maryland</option>
                    <option value="MA">Massachusetts</option>
                    <option value="MI">Michigan</option>
                    <option value="MN">Minnesota</option>
                    <option value="MS">Mississippi</option>
                    <option value="MO">Missouri</option>
                    <option value="MT">Montana</option>
                    <option value="NE">Nebraska</option>
                    <option value="NV">Nevada</option>
                    <option value="NH">New Hampshire</option>
                    <option value="NJ">New Jersey</option>
                    <option value="NM">New Mexico</option>
                    <option value="NY">New York</option>
                    <option value="NC">North Carolina</option>
                    <option value="ND">North Dakota</option>
                    <option value="OH">Ohio</option>
                    <option value="OK">Oklahoma</option>
                    <option value="OR">Oregon</option>
                    <option value="PA">Pennsylvania</option>
                    <option value="RI">Rhode Island</option>
                    <option value="SC">South Carolina</option>
                    <option value="SD">South Dakota</option>
                    <option value="TN">Tennessee</option>
                    <option value="TX">Texas</option>
                    <option value="UT">Utah</option>
                    <option value="VT">Vermont</option>
                    <option value="VA">Virginia</option>
                    <option value="WA">Washington</option>
                    <option value="WV">West Virginia</option>
                    <option value="WI">Wisconsin</option>
                    <option value="WY">Wyoming</option>
                </select> <br/>

                <label for="zipCode">Zip Code</label> <br/>
                <input type="text" id="zipCode" name="profile" maxlength = "9" minlength = "5" required /> <br/>
                
            </form>

        </div>
      
                
           
            <div >
                <button id="reset-btn" type="reset" className="toggle-btn"> Go Back </button>
                <button id="save-btn" type="save" className="toggle-btn"> Save </button>
            
            </div>
        
    </div>
  );
}

export default ClientProfile;
