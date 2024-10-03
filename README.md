# Weekly-Diet-Plan-Generator
This project is a Flask-based user-friendly web application designed to generate a personalized seven-day diet plan according to user inputs. The application allows users to enter their personal information, dietary preferences, medical conditions, and fitness goals through a chatbot interface. 

### Key Components and Features

1. **User Input and Data Collection**:
   - The application utilizes a chatbot interface where users provide personal information, including: Full Name, Age, Gender, Weight, Medical Conditions, Dietary Preferences including the number of meals per day, specific fitness goals (like weight loss, muscle gain, etc.) and any allergies and Dietary Restrictions such as vegetarian, vegan, or gluten-free preferences.

2. **Database Management**:
   - The application employs **SQLite** as the database to store user data and diet plans. This includes:
     - **Diet Plan Table** (`dietplan`): Stores user profiles and their dietary needs.
     - **Meals Table** (`meals`): Contains individual meal entries linked to the corresponding diet plan.
   - The database is initialized at the start of the application, ensuring all necessary tables are created.

3. **Meal Plan Generation**:
   - The application generates a **weekly meal plan** consisting of breakfast, lunch, and dinner for each day of the week. 
   - The meal selection process involves:
     - **Filtering Meal Options**: Based on user-defined dietary restrictions and allergies. 
     - **Random Selection**: To ensure variety, meals are randomly selected from the filtered options for each meal type.
   - Example meals include oatmeal, quinoa salad, baked salmon, and vegan chili, catering to various dietary needs.

4. **Error Handling and Logging**:
   - The application incorporates robust error handling to manage situations such as missing required information or no available meal options based on user constraints. 
   - Debugging statements log key actions and errors, aiding in troubleshooting during development.

5. **Dynamic Content Serving**:
   - Flask's templating engine is utilized to dynamically render HTML pages:
     - **Main Page**: Serves as the entry point for users.
     - **Diet Plan Page**: Displays the most recent diet plan, including details for each meal, organized by day.
     - **Benefits Pages**: Separate pages that provide information on the importance of meal planning and regular exercise.


### Technologies Used
- **Flask**: The web framework that provides the structure for building the application.
- **SQLite**: Database for storing user data and meal plans.
- **HTML/CSS**: For creating and styling the web pages, making the application visually appealing.
- **JavaScript**: Used for interactive features.
