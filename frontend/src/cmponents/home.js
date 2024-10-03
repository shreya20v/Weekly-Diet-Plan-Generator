import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div className="home">
            <h1>Plan Your Health</h1>
            <button>
                <Link to="/diet-plan">Create Your Personalized Diet Plan</Link>
            </button>
            <div className="links">
                <Link to="/benefits">Benefits of Meal Planning</Link>
                <Link to="/exercise">Benefits of Exercising</Link>
            </div>
        </div>
    );
};

export default Home;
