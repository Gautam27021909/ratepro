import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation
import './SignupPage.css';

const SignupPage = () => {
    const navigate = useNavigate(); // Create navigate function

    // Function to handle form submission
    const handleContinueClick = (event) => {
        event.preventDefault(); // Prevent default form submission
        navigate('/landing'); // Navigate to the LandingPage
    };

   
};

export default SignupPage;
