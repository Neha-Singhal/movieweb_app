from sqlalchemy.exc import SQLAlchemyError
from .data_manager_interface import DataManagerInterface
from .data_models import User, Movie, db
from flask import current_app


class SQLiteDataManager(DataManagerInterface):
    """SQLAlchemy implementation of DataManagerInterface"""

    def __init__(self, db_instance):
        self.db = db_instance  # This should be the SQLAlchemy instance from data_models

    def get_all_users(self):
        """Fetch all users"""
        try:
            return User.query.all()
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error getting users: {e}")
            self.db.session.rollback()
            return []

    def get_user_movies(self, user_id):
        """Fetch movies for a specific user"""
        try:
            return Movie.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error getting movies: {e}")
            self.db.session.rollback()
            return []

    def get_movie_by_id(self, movie_id):
        """Fetch a single movie by movie_id"""
        try:
            return self.db.session.get(Movie, movie_id)  # New SQLAlchemy 2.0 style
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error getting movie {movie_id}: {e}")
            self.db.session.rollback()
            return None

    def add_user(self, user_name):
        """Add a new user if they don't exist"""
        try:
            if User.query.filter_by(user_name=user_name).first():
                return None

            new_user = User(user_name=user_name)
            self.db.session.add(new_user)
            self.db.session.commit()
            return new_user
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error adding user: {e}")
            self.db.session.rollback()
            return None

    def add_movie(self, user_id, movie_name, movie_director,
                  movie_year, movie_rating, movie_poster):
        """Add a new movie if it doesn't exist"""
        try:
            if Movie.query.filter_by(movie_name=movie_name).first():
                return None

            new_movie = Movie(
                movie_name=movie_name,
                movie_director=movie_director,
                movie_year=movie_year,
                movie_rating=movie_rating,
                movie_poster=movie_poster,
                user_id=user_id
            )
            self.db.session.add(new_movie)
            self.db.session.commit()
            return new_movie
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error adding movie: {e}")
            self.db.session.rollback()
            return None

    def update_movie(self, user_id, movie_id, movie_name,
                     movie_director, movie_year, movie_rating):
        """Update movie details"""
        try:
            movie = self.db.session.get(Movie, movie_id)
            if not movie:
                return None

            movie.movie_name = movie_name
            movie.movie_director = movie_director
            movie.movie_year = movie_year
            movie.movie_rating = movie_rating
            self.db.session.commit()
            return movie
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error updating movie: {e}")
            self.db.session.rollback()
            return None

    def delete_movie(self, user_id, movie_id):
        """Delete a movie"""
        try:
            movie = self.db.session.get(Movie, movie_id)
            if movie:
                self.db.session.delete(movie)
                self.db.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error deleting movie: {e}")
            self.db.session.rollback()
            return False

    def best_movies(self):
        """Get top 5 movies by rating"""
        try:
            return Movie.query.order_by(Movie.movie_rating.desc()).limit(5).all()
        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error getting best movies: {e}")
            return []