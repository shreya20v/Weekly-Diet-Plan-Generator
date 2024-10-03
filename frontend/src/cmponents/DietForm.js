import React, { useState } from 'react';

const DietForm = () => {
    const [preferences, setPreferences] = useState('');
    const [restrictions, setRestrictions] = useState('');
    const [goals, setGoals] = useState('');
    const [mealPlan, setMealPlan] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: `preferences: ${preferences}, restrictions: ${restrictions}, goals: ${goals}` })
        });
        const data = await response.json();
        setMealPlan(data.response);
    };

    return (
        <div className="diet-form">
            <h2>Create Your Personalized Diet Plan</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Preferences:
                    <input type="text" value={preferences} onChange={(e) => setPreferences(e.target.value)} />
                </label>
                <label>
                    Restrictions:
                    <input type="text" value={restrictions} onChange={(e) => setRestrictions(e.target.value)} />
                </label>
                <label>
                    Goals:
                    <input type="text" value={goals} onChange={(e) => setGoals(e.target.value)} />
                </label>
                <button type="submit">Submit</button>
            </form>
            {mealPlan && <div className="meal-plan">{mealPlan}</div>}
        </div>
    );
};

export default DietForm;

