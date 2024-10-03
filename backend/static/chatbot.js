document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const chatInput = document.getElementById('chat-input');

    let userData = {};

    const questions = [
        { question: 'What is your full name?', type: 'input', inputType: 'text' },
        { question: 'What is your age?', type: 'input', inputType: 'number' },
        { question: 'What is your gender?', type: 'dropdown', options: ['Male', 'Female', 'Others'] },
        { question: 'Do you have any dietary restrictions?', type: 'dropdown', options: ['None', 'Vegetarian', 'Vegan', 'Gluten-Free', 'Dairy-Free'] },
        { question: 'What are your fitness goals?', type: 'dropdown', options: ['Lose Weight', 'Gain Muscle', 'Maintain Weight', 'Improve Stamina'] },
        { question: 'How many meals do you prefer per day?', type: 'dropdown', options: ['3', '4', '5'] },
        { question: 'Do you have any food allergies?', type: 'dropdown', options: ['None', 'Nuts', 'Fish', 'Dairy', 'Gluten'] },
        { question: 'What is your body weight (in kg)?', type: 'input', inputType: 'number' },
        { question: 'Do you have any medical conditions or history?', type: 'dropdown', options: ['None','Diabetes', 'High Blood Pressure', 'Lung Disease', 'High Cholesterol', 'Other'] },
        { question: 'Please specify your medical condition (if you selected "Other"):', type: 'input', inputType: 'text', conditional: 'Do you have any medical conditions or history?' }
    ];

    let currentQuestion = 0;

    function createDropdown(question) {
        const select = document.createElement('select');
        select.id = 'user-input';
        question.options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            select.appendChild(optionElement);
        });
        return select;
    }

    function createInput(question) {
        const input = document.createElement('input');
        input.id = 'user-input';
        input.type = question.inputType;
        return input;
    }

    function scrollToBottom() {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function askQuestion() {
        if (currentQuestion < questions.length) {
            const question = questions[currentQuestion];
            chatBox.innerHTML += `<p>${question.question}</p>`;
            chatInput.innerHTML = '';

            if (question.type === 'dropdown') {
                const dropdown = createDropdown(question);
                chatInput.appendChild(dropdown);
            } else if (question.type === 'input') {
                const input = createInput(question);
                chatInput.appendChild(input);
            }

            const submitButton = document.createElement('button');
            submitButton.textContent = 'Submit';
            submitButton.id = 'submit-button'; // Add an ID for CSS targeting
            submitButton.onclick = () => {
                const userInput = document.getElementById('user-input').value;
                userData[question.question] = userInput;
                chatBox.innerHTML += `<p><strong>You entered:</strong> ${userInput}</p>`;

                // Check for conditional input field
                if (question.conditional && userInput !== 'Other') {
                    currentQuestion++; // Skip the next question if condition is not met
                }

                currentQuestion++;
                scrollToBottom();
                askQuestion();
            };
            chatInput.appendChild(submitButton);

            scrollToBottom(); // Scroll to bottom when a new question is displayed
        } else {
            chatBox.innerHTML += '<p>Thank you for providing your information. Your diet plan is being created.</p>';
            const viewPlanButton = document.createElement('a');
            viewPlanButton.href = '/diet-plan'; // Change this URL to where the generated diet plan is located
            viewPlanButton.textContent = 'View Your Diet Plan';
            viewPlanButton.className = 'view-plan-button';
            chatBox.appendChild(viewPlanButton);
            scrollToBottom(); // Scroll to bottom after displaying the final message

            submitData(userData); // Submit the collected data to the server
        }
    }

    function submitData(data) {
        fetch('/create-diet-plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<p>${data.message}</p>`;
            scrollToBottom(); // Scroll to bottom after displaying the final message
        })
        .catch(error => {
            console.error('Error:', error);
            chatBox.innerHTML += '<p>There was an error generating your diet plan.</p>';
            scrollToBottom(); // Scroll to bottom after displaying the error message
        });
    }

    askQuestion();
});
