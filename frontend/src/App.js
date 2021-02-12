import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch, Link, Redirect } from "react-router-dom";

// styles
import './App.css';

// pages
import MainPage from "./pages";

class App extends Component { 
    render() {
        return ( 
        <Router> 
            <Route path="/" component={MainPage}/>
        </Router>
        );
    }
} 

export default App;
