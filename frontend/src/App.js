import React, { useState, useEffect } from "react";
import logo from './logo.svg';
/* import './App.css'; */
import NavBar from './NavBar';
import Home from './Home';

import { 
    BrowserRouter as Router,
    Switch,
    Route, 
    Link
    } from "react-router-dom";

export default function App() {
    const [currentTime, setCurrentTime] = useState(0);

    useEffect(() => {
        fetch('http://lacuna.columbiadpi.com/api/test').then(res => res.json()).then(data => {
            setCurrentTime(data.test);
        });
    }, []);
    
    return (
    <div>
        <Home />
    </div>
    );
}

