import random

def generate_meal_plan(preferences, restrictions, goals):
    meals = [
        {"meal": "Oatmeal with fruits", "calories": 350},
        {"meal": "Chicken salad", "calories": 400},
        {"meal": "Quinoa and vegetables", "calories": 450}
    ]
    return random.choice(meals)
