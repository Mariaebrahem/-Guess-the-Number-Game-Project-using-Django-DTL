✅ Project Idea:

A simple web game where the user tries to guess a number between 1 and 10.
After submitting a guess, the app tells the user if their guess is correct, or if the number is higher or lower.

🎯 Project Goals:

Use Django Template Language (DTL) to dynamically render content.

Apply:

Variables → {{ variable }}

Filters → |default, |safe

Tags → {% if %}, {% csrf_token %}

🗂️ Project Structure:
1. HTML Template

📄 templates/pages/home.html

Includes:

A form for user input

Displays the last guess

Shows the result message (correct, too low, too high)

2. View (Logic)

📄 views.py

Handles POST request and receives user input.

Compares the guess to the correct number.

Sends result data back to the template.

3. URL Configuration

📄 urls.py

Page route is typically / or /game/.

🧩 DTL Elements Used:
Feature	Example
Variables	{{ message }}, {{ guess }}
Filters	`
Tags	{% if %}, {% csrf_token %}
