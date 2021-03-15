import React from 'react';
import '../App.css';
import './client.css';

function FuelQuoteForm() {
  return (
    <div > 
        <h1> Fuel Quote Form Page</h1>
        <div className ="login"> {/* removed this class temporarily --> className="form-wrap"> */}
		
            <form id="my-form">

                <div>
                    <label for="gallons">Gallons Requested:</label>
                    <input id="gallons" type="number" />
                </div>

                <div>
                    <label for="date">Delivery Date:</label>
                    <input id="date" type="date" />
                </div>

                <div>
                    <label for="address">Address:</label>
                    <input id="address" type="text" />
                </div>

                <div>
                    <label for="price">Price Per Gallon:</label>
                    <input id="price" type="number" />
                </div>
                

                <div>
                    <label for="total">Total Amount Due:</label>
                    <input id="total" type="number" />
                </div>

                <div>
                    <input id="save" type="submit" value="Save Changes" disabled />
                </div>

            </form>
	    </div>
    </div>
  );
}

export default FuelQuoteForm;
