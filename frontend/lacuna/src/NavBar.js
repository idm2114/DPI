import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';
import Home from './Home';
import CollectEmail from './CollectEmail';
import { 
    BrowserRouter as Router,
    Switch,
    Route, 
    Link
    } from "react-router-dom";

export default function NavBar() {
    const [username, setUsername] = useState(0);

    useEffect(() => {
        fetch('http://lacuna.columbiadpi.com/api/test').then(res => res.json()).then(data => {
            setCurrentTime(data.test);
        });
    }, []);
    
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/createEmail">CreateEmail</Link>
                        </li>
                    </ul>
                </nav>
                
                <Switch>
                  <Route path="/createEmail">
                    <CollectEmail />
                  </Route>
                  <Route path="/">
                    <Home />
                  </Route>
                </Switch>
          </div>
    </Router>
    );
}
