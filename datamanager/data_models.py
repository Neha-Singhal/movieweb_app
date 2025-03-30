from enum import unique
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class User(db.Model):
    """
    Represents a User in the database.
    """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String, unique=True)

    movies = db.relationship('Movie', back_populates='user', lazy=True)

    def __repr__(self):
        """
        Returns a string representation of the User object.
        """
        return f"User(id={self.user_id}, user_name={self.user_name})"


class Movie(db.Model):
    """
    Represents a Movie in the database.
    """
    __tablename__ = 'movies'
    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column(db.String,unique=True)
    movie_director = db.Column(db.String)
    movie_year = db.Column(db.Integer)
    movie_rating = db.Column(db.Float)
    movie_poster = db.Column(db.String)

    # Foreign key to associate the movie with a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    # Define the relationship explicitly with back_populates
    user = db.relationship('User', back_populates='movies', lazy=True)

    def __repr__(self):
        """
        Returns a string representation of the Movie object.
        """
        return f"Movie(id={self.movie_id}, movie_name={self.movie_name})"