import React from 'react';
import '../App.css';
import './client.css';

function FuelQuoteForm() {
  return (
    <div > 
        <h1> Fuel Quote Form Page</h1>

        <table className="center">
            <tr>
                <th>Gallons</th>
                <th>Delivery Date</th>
                <th>Address</th>
                <th>Price Per Gallon</th>
                <th>Total Amount Due</th>
            </tr>
            <tr>
                <td>55</td>
                <td>11/11/2011</td>
                <td>1111 Big Ln</td>
                <td>0.99</td>
                <td>10999</td>
            </tr>
             <tr>
                <td>10000</td>
                <td>11/11/2023</td>
                <td>1111 Small Ln</td>
                <td>0.99</td>
                <td>109999999</td>
            </tr>
        </table>


    </div>
  );
}

export default FuelQuoteForm;
