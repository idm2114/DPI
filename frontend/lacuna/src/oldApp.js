import React, { Component, useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Switch, Link, Redirect } from "react-router-dom";
import BubbleChart from '@weknow/react-bubble-chart-d3';

// styles
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

// pages
import MainPage from "./pages";
import NotFound from "./pages";
import Login from "./pages/login";
import Home from "./pages/home";
import Class from "./pages/class";

class App extends Component { 
    render() {
        return ( 
        <Router> 
            <Switch>
                <Route exact path="/" component={MainPage}/>
                <Route exact path="/login">
                    <Login />
                </Route>
                // fix this so it works in react
                // user
                <Route exact path="/home/<userid>">
                    <Home />
                </Route>
                // class 
                // class page 
                <Route exact path="/class/<classid>">
                    <Class />
                </Route>
                <Route component={NotFound}/>
                <Redirect to="/404"/>
            </Switch>
        </Router>
        );
    }
} 

export default App;
