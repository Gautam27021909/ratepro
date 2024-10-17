import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css';

const LoginPage = () => {
    const navigate = useNavigate(); 

    const handleLogin = (e) => {
        e.preventDefault();
       
        navigate('/landing');
    };

};

export default LoginPage;
