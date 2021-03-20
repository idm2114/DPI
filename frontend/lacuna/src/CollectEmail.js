import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import NavBar from './NavBar';

export default function collectEmail() {
    
    const onSubmit = event => {
        event.preventDefault();
        alert('You have submitted this form');
    }

    return (
        <div>
            <header>
            <h1> We look forward to showing you our website! </h1>
            </header>
            <h3> Please enter your email: </h3>
            <form onSubmit = {onSubmit}>
                <input type="email" name="email" required />
                <input type="submit" />
            </form>
        </div>
    );
}
