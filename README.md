# movieweb_app

MoviWeb is a Flask-based web application that allows users to manage their movie collections. It features a user-friendly interface for adding, updating, deleting, and listing movies. The backend is powered by SQLite and SQLAlchemy for efficient data management.

Features

User selection and management

Add, update, and delete movies

Store movie details (name, director, year, rating)

Persistent storage using SQLite

Web interface built with Flask and Jinja templates

Technologies Used

Backend: Python, Flask, SQLAlchemy, SQLite

Frontend: HTML, CSS, Jinja2

Other: Flask-CORS, Bootstrap (for styling)

Installation

Prerequisites

Ensure you have Python installed (preferably Python 3.8+).

Clone the Repository
 https://github.com/Neha-Singhal/movieweb_app.git
Install Dependencies
pip install -r requirements.txt
S
et up the .env file for storing the API key (OMDb API):

Create a file named .env in the config directory.
Add your OMDb API key to the file:
API_KEY=your_omdb_api_key_here
Run the Flask app:

python app.py
Routes

/: Home page displaying the top 5 rated movies.
/users: View all users.
/users/<user_id>: View movies of a specific user.
/add_user: Add a new user.
/users/<user_id>/add_movie: Add a movie to a user's collection.
/users/<user_id>/update_movie/<movie_id>: Update movie details.
/users/<user_id>/delete_movie/<movie_id>: Delete a movie from a user's collection.
Database Structure The application uses SQLAlchemy with SQLite as the database backend. There are two main models:

User: Represents a user with a unique user_name.
Movie: Represents a movie in a user's collection with attributes like movie_name, movie_director, movie_year, movie_rating, and movie_poster. Each movie is associated with a specific user.
Error Handling

The application includes custom error pages for:

404: Page not found.

505: Internal server error.





