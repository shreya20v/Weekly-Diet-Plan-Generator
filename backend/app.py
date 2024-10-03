from flask import Flask, render_template, send_from_directory, jsonify, request
import sqlite3
import random

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')

# Function to initialize the database
def init_db():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        # Create dietplan table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dietplan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pname TEXT,
                age INTEGER,
                gender TEXT,
                weight INTEGER,
                condition TEXT,
                diet TEXT,
                goal TEXT,
                allergies TEXT
            )
        """)
        # Create meals table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dietplan_id INTEGER,
                day TEXT,
                meal_type TEXT,
                description TEXT,
                items TEXT,
                FOREIGN KEY(dietplan_id) REFERENCES dietplan(id)
            )
        """)
        conn.commit()

# Initialize the database
init_db()

# Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Serve any other static files (like CSS, images, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Sample meals with dietary restrictions and allergens
breakfast_options = [
    {"meal": "Oatmeal with fruits", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Maintain Weight", "Lose Weight"]},
    {"meal": "Smoothie bowl", "restrictions": ["Vegetarian", "Vegan"], "allergens": [], "health_conditions": ["Diabetes"], "fitness_goals": ["Lose Weight", "Improve Stamina"]},
    {"meal": "Scrambled eggs with spinach", "restrictions": ["Vegetarian"], "allergens": [], "health_conditions": [], "fitness_goals": ["Gain Muscle", "Maintain Weight"]},
    {"meal": "Avocado toast", "restrictions": ["Vegetarian"], "allergens": ["Gluten"], "health_conditions": [], "fitness_goals": ["Maintain Weight"]},
    {"meal": "Chia pudding", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Lose Weight"]},
    {"meal": "Greek yogurt with honey and nuts", "restrictions": ["Vegetarian"], "allergens": ["Dairy", "Nuts"], "health_conditions": [], "fitness_goals": ["Gain Muscle", "Maintain Weight"]},
    {"meal": "Banana pancakes", "restrictions": ["Vegetarian", "Vegan"], "allergens": ["Gluten"], "health_conditions": [], "fitness_goals": ["Lose Weight"]},
    {"meal": "Egg white omelet with bell peppers", "restrictions": ["Vegetarian"], "allergens": [], "health_conditions": [], "fitness_goals": ["Gain Muscle", "Maintain Weight"]},
    {"meal": "Fruit salad with nuts", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": ["Nuts"], "health_conditions": [], "fitness_goals": ["Maintain Weight", "Lose Weight"]},
    {"meal": "Peanut butter and banana smoothie", "restrictions": ["Vegetarian", "Vegan"], "allergens": ["Peanuts"], "health_conditions": [], "fitness_goals": ["Gain Muscle"]},
]

lunch_options = [
    {"meal": "Quinoa salad", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Lose Weight", "Maintain Weight"]},
    {"meal": "Grilled chicken with vegetables", "restrictions": ["Gluten-Free"], "allergens": [], "health_conditions": ["High Blood Pressure"], "fitness_goals": ["Gain Muscle"]},
    {"meal": "Lentil soup", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Lose Weight"]},
    {"meal": "Veggie wrap", "restrictions": ["Vegetarian"], "allergens": ["Gluten"], "health_conditions": [], "fitness_goals": ["Maintain Weight"]},
    {"meal": "Stir-fried tofu with rice", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Gain Muscle", "Vegan"]},
    {"meal": "Chickpea salad", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Maintain Weight", "Lose Weight"]},
    {"meal": "Pasta primavera", "restrictions": ["Vegetarian"], "allergens": ["Gluten"], "health_conditions": [], "fitness_goals": ["Maintain Weight"]},
    {"meal": "Fish tacos with cabbage slaw", "restrictions": ["Gluten-Free"], "allergens": ["Fish"], "health_conditions": [], "fitness_goals": ["Gain Muscle"]},
    {"meal": "Mushroom risotto", "restrictions": ["Vegetarian"], "allergens": ["Dairy"], "health_conditions": [], "fitness_goals": ["Maintain Weight"]},
    {"meal": "Vegetable sushi rolls", "restrictions": ["Vegetarian", "Vegan"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Lose Weight"]},
]

dinner_options = [
    {"meal": "Baked salmon with asparagus", "restrictions": ["Gluten-Free"], "allergens": ["Fish"], "health_conditions": ["High Cholesterol"], "fitness_goals": ["Gain Muscle"]},
    {"meal": "Veggie stir-fry with noodles", "restrictions": ["Vegetarian", "Vegan"], "allergens": ["Gluten"], "health_conditions": [], "fitness_goals": ["Vegan", "Maintain Weight"]},
    {"meal": "Chicken curry with rice", "restrictions": ["Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Gain Muscle"]},
    {"meal": "Vegan chili", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Lose Weight"]},
    {"meal": "Stuffed bell peppers", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Maintain Weight"]},
    {"meal": "Baked tofu with sweet potatoes", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Lose Weight"]},
    {"meal": "Shrimp stir-fry with vegetables", "restrictions": ["Gluten-Free"], "allergens": ["Shellfish"], "health_conditions": [], "fitness_goals": ["Gain Muscle"]},
    {"meal": "Vegetable curry with brown rice", "restrictions": ["Vegetarian", "Vegan"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Maintain Weight"]},
    {"meal": "Beef and broccoli stir-fry", "restrictions": ["Gluten-Free"], "allergens": [], "health_conditions": ["High Blood Pressure"], "fitness_goals": ["Gain Muscle"]},
    {"meal": "Lentil and vegetable shepherd's pie", "restrictions": ["Vegetarian", "Vegan", "Gluten-Free"], "allergens": [], "health_conditions": [], "fitness_goals": ["Vegan", "Lose Weight"]},
]

# Define route for creating a diet plan
@app.route('/create-diet-plan', methods=['GET', 'POST'])
def create_diet_plan():
    if request.method == 'POST':
        try:
            data = request.json
            print("Received data from chatbot:", data)  # Debugging: Check received data

            # Extract data from JSON
            pname = data.get('What is your full name?')
            age = data.get('What is your age?')
            gender = data.get('What is your gender?')
            weight = data.get('What is your body weight (in kg)?')
            condition = data.get('Do you have any medical conditions or history?')
            diet = data.get('How many meals do you prefer per day?')
            goal = data.get('What are your fitness goals?')
            allergies = data.get('Do you have any food allergies?')
            restrictions = data.get('Do you have any dietary restrictions?')

            # Debugging: Log parsed data
            print("Parsed data:", pname, age, gender, weight, condition, diet, goal, allergies, restrictions)
            
            # Check for missing required fields
            if not all([pname, gender, condition, diet, goal, allergies]):
                raise ValueError("Missing required data fields")

            # Handle missing optional fields
            age = int(age) if age else None
            weight = int(weight) if weight else None

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                
                # Insert diet plan data
                cur.execute("""
                    INSERT INTO dietplan (pname, age, gender, weight, condition, diet, goal, allergies)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (pname, age, gender, weight, condition, diet, goal, allergies))
                dietplan_id = cur.lastrowid
                print("Inserted diet plan with ID:", dietplan_id)  # Debugging: Check inserted ID

                # Generate and insert weekly meal plan
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                meal_plan = []
                for day in days:
                    daily_meals = {
                        "day": day,
                        "meals": []
                    }
                    for meal_type in ["Breakfast", "Lunch", "Dinner"]:
                        # Filter meal options based on dietary restrictions and allergies
                        if meal_type == "Breakfast":
                            filtered_options = [meal for meal in breakfast_options if restrictions in meal["restrictions"] and not any(allergy in meal["allergens"] for allergy in allergies)]
                        elif meal_type == "Lunch":
                            filtered_options = [meal for meal in lunch_options if restrictions in meal["restrictions"] and not any(allergy in meal["allergens"] for allergy in allergies)]
                        else:  # Dinner
                            filtered_options = [meal for meal in dinner_options if restrictions in meal["restrictions"] and not any(allergy in meal["allergens"] for allergy in allergies)]
                        
                        if not filtered_options:
                            raise ValueError(f"No available {meal_type} options for {day} that meet the dietary restrictions and allergies.")
                        
                        selected_meal = random.choice(filtered_options)
                        items = selected_meal["meal"]
                        description = f"{meal_type} for {day}"
                        daily_meals["meals"].append({
                            "meal_type": meal_type,
                            "description": description,
                            "items": items
                        })
                        cur.execute("""
                            INSERT INTO meals (dietplan_id, day, meal_type, description, items)
                            VALUES (?, ?, ?, ?, ?)
                        """, (dietplan_id, day, meal_type, description, items))
                        print(f"Inserted {meal_type} for {day} with items: {items}")  # Debugging: Check meal insertion
                    meal_plan.append(daily_meals)
                conn.commit()

            return render_template('diet_plan.html', user_data=data, meal_plan=meal_plan)
        except Exception as e:
            print("Error occurred:", e)  # Debugging: Print error
            return jsonify({"error": str(e)}), 500
    return render_template('create_diet_plan.html')


# Define route for viewing diet plans
@app.route('/diet-plan')
def diet_plan():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        # Fetch the last diet plan
        cur.execute("SELECT * FROM dietplan ORDER BY id DESC LIMIT 1")
        last_diet_plan = cur.fetchone()
        if last_diet_plan:
            cur.execute("SELECT day, meal_type, description, items FROM meals WHERE dietplan_id = ?", (last_diet_plan[0],))
            meals = cur.fetchall()
            meals_by_day = {}
            for meal in meals:
                if meal[0] not in meals_by_day:
                    meals_by_day[meal[0]] = []
                meals_by_day[meal[0]].append(meal)
            diet_plan_with_meals = {
                'dietplan': last_diet_plan,
                'meals': meals_by_day
            }
        else:
            diet_plan_with_meals = None

    return render_template('diet_plan.html', diet_plan=diet_plan_with_meals)

# Define route for benefits of meal planning
@app.route('/benefits-meal-planning')
def benefits_meal_planning():
    return render_template('benefits_meal_planning.html')

# Define route for benefits of exercising
@app.route('/benefits-exercising')
def benefits_exercising():
    return render_template('benefits_exercising.html')

@app.route('/view-db')
def view_db():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM dietplan ORDER BY id DESC LIMIT 1")
        last_entry = cur.fetchone()
    return jsonify(last_entry)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
