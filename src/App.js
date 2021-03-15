import React from 'react';
import './App.css';

import Nav from './pages/Nav';
import About from './pages/About';
import Shop from './pages/Shop';
import ClientProfile from './pages/ClientProfile';
import LoginPage from './pages/LoginPage';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import ForgotPassword from './pages/ForgotPassword';
import NewPassword from './pages/NewPassword';
import ConfirmPassReset from './pages/ConfirmPassReset';
import FuelQuoteForm from './pages/FuelQuoteForm';
import FuelQuoteHistory from './pages/FuelQuoteHistory';


function App() {
  return (
    <Router>
      <div className="App">
        <Nav>  </Nav>
        <Switch>
            <Route path = "/" exact component={Home} /> {/* maybe / should be the login page... */}
  
            <Route path = "/about" component={About} /> 
            <Route path = "/shop" component={Shop} /> 
            <Route path = "/profile" component={ClientProfile} />
            <Route path = "/login" component={LoginPage} />
            <Route path = "/forgot" component={ForgotPassword} />
            <Route path = "/setnewpassword" component={NewPassword} />
            <Route path = "/passwordreset" component={ConfirmPassReset} />
            <Route path = "/fuelquoteform" component={FuelQuoteForm} />
            <Route path = "/fuelquotehistory" component={FuelQuoteHistory} />




        </Switch>
          
      </div>
    </Router>
      
      
  );
}

const Home = () =>(
  
  <div>
    <h1> Home page </h1>

  </div>
  
)



export default App;

