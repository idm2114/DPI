import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';
import NavBar from './NavBar';

export default function Home() {
    return (
        <div>
            <div className="App-header">
                <header className="App-header">
                <h1> Welcome to Lacuna! </h1>
                <h3> We are remodeling, click <a href='/collectEmail'>here</a> to be notified when construction is done! </h3>
                </header>
            </div>
        </div>
    );
}
