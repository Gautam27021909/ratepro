import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css';

const LoginPage = () => {
    const navigate = useNavigate();  // To handle navigation after login

    const handleLogin = (e) => {
        e.preventDefault();
        // Logic for handling login, like authentication
        // After successful login:
        navigate('/landing');  // Navigate to the landing page after login
    };

};

export default LoginPage;
