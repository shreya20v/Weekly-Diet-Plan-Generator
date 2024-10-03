import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import DietForm from './components/DietForm';
import Benefits from './components/Benefits';
import Exercise from './components/Exercise';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/diet-plan" element={<DietForm />} />
                <Route path="/benefits" element={<Benefits />} />
                <Route path="/exercise" element={<Exercise />} />
            </Routes>
        </Router>
    );
};

export default App;
