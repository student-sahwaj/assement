Project Overview

This project is a FastAPI-based web application developed as part of the technical assessment for the Python Developer Intern position at Qixbi Technologies. The objective is to demonstrate proficiency in Python, FastAPI, and database management by implementing user authentication via Google OAuth and providing CRUD operations for managing stock watchlists.

Features

Authentication System:

Implemented Google OAuth 2.0 integration.

Stored authenticated user information.

Created secure session management.

Protected routes for authorized users.

CRUD Operations for Watchlists:

Create, read, update, and delete watchlist entries.

List all watchlist entries for the logged-in user.

Database Management:

PostgreSQL database with SQLAlchemy ORM for database interactions.

Two tables: User and Watchlist.

API Documentation:

Automatic API documentation using Swagger/OpenAPI.

Additional Features:

Input validation and error handling.

RESTful API design principles.

Environment variable management for sensitive credentials.

Setup Instructions

Prerequisites

Python 3.8+

PostgreSQL database

A Google Cloud project with OAuth credentials

Installation

Clone the repository:

git clone https://github.com/your-repo-url
cd your-repo-folder

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory with the following content:

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
DATABASE_URL=postgresql://username:password@localhost/your_db
SECRET_KEY=your_secret_key

Apply database migrations:

alembic upgrade head

Start the application:

uvicorn app.main:app --reload

Running the Application

Open your browser and navigate to http://127.0.0.1:8000 to access the application.

API documentation is available at http://127.0.0.1:8000/docs.

API Endpoints

Authentication Endpoints

GET /auth/google/login - Redirect to Google for authentication.

GET /auth/google/callback - Handle the callback after Google authentication.

GET /auth/logout - Logout the user.

Watchlist CRUD Endpoints

POST /watchlist/ - Create a new watchlist entry.

GET /watchlist/ - List all entries for the logged-in user.

GET /watchlist/{id} - Get details of a specific watchlist entry.

PUT /watchlist/{id} - Update an existing watchlist entry.

DELETE /watchlist/{id} - Delete a watchlist entry.

Project Structure

.
├── app/
│   ├── main.py           # Application entry point
│   ├── auth.py           # Google OAuth authentication
│   ├── models.py         # Database models
│   ├── database.py       # Database configuration
│   ├── crud.py           # Database operations
│   ├── schemas.py        # Pydantic schemas
├── .env                   # Environment variables (not committed to Git)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

Deliverables

Source Code:

GitHub repository with a properly structured project layout and clear commit history.

Documentation:

README.md with:

Project overview

Setup instructions

API documentation

Environment variables list

Development decisions and assumptions

Requirements:

requirements.txt file for dependencies.

.env.example template for environment variables.

Evaluation Criteria

Core Assessment (80%)

Authentication implementation (20%)

CRUD operations (20%)

Database design and implementation (10%)

Code organization and quality (10%)

Error handling and input validation (10%)

API Documentation (10%)

Additional Factors (20%)

Documentation quality (10%)

Git usage and commit quality (5%)

Extra features/improvements (5%)

Bonus Points

Unit tests

API rate limiting

Response caching

Advanced error handling

Comprehensive type hinting
