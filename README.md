# Fitness App

This Django-based RESTful API allows users to manage personalized workout plans and track fitness goals.

## Setup

### Prerequisites
- Python 3.x installed on your system
- Virtual environment tool (e.g., virtualenv or pipenv)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fitness-app.git

2. Navigate to the project directory:
   cd fitness-app

3. Create a virtual environment:
    # Using virtualenv
    virtualenv venv
    # Activate the virtual environment
    source venv/bin/activate

    # Using pipenv
    pipenv install

4. Install dependencies:
    pip install -r requirements.txt

5. Apply database migrations:
    python manage.py migrate

6. Run the development server:
    python manage.py runserver

Usage
API Documentation
The API endpoints are documented using Swagger/OpenAPI. You can access the documentation by navigating to http://localhost:8000/swagger/ in your web browser while the development server is running.

User Authentication
The API supports user registration, login, and logout using JWT (JSON Web Tokens) for secure session management. Here's how you can interact with the authentication endpoints:

Register: POST /api/register/

Create a new user account by providing username, email, and password.
Login: POST /api/login/

Obtain JWT tokens (access token and refresh token) by providing valid credentials (username/email and password).
Logout: POST /api/logout/

Log out the user and invalidate the refresh token.
Personalized Workout Plans
The API allows users to create tailored workout plans, select exercises, and track fitness goals. You can interact with the workout planning endpoints to manage your workout routines and track progress.



