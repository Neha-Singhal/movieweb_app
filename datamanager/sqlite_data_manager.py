from sqlalchemy.exc import SQLAlchemyError
from .data_manager_interface import DataManagerInterface
from .data_models import User, Movie, db

class SQLiteDataManager(DataManagerInterface):
    """The SQLiteDataManager is the  implementation of the DataManagerInterface"""
    def __init__(self, app, db_file_name):
        self.app = app
        self.db_file_name = db_file_name

        # Flask app config for SQLAlchemy
        app.config['SQLALCHEMY_DATABASE_URI'] = db_file_name

        # Initialize SQLAlchemy with the app
        self.db = db
        db.init_app(app)

        # Create the tables if they don't already exist
        with app.app_context():
            db.create_all()

    def get_all_users(self):
        """
        Query to fetch all users
        """
        try:
            with self.app.app_context():
                users = User.query.all()  # Using ORM query
            return users

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Data base error: {e}")
            return []

    def get_user_movies(self, user_id):
        """
        Query to fetch movies for a specific user
        """
        try:
            with self.app.app_context():
                movies = Movie.query.filter_by(user_id = user_id).all()
            return movies
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Data base error to get movies: {e}")
            return []

    def get_movie_by_id(self, movie_id):
        """
        Query to fetch a single movie by movie_id
        """
        try:
            with self.app.app_context():
                # Fetch the movie by movie_id
                movie = Movie.query.filter_by(movie_id = movie_id).first()
            return movie

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Data base error to get movies for {movie_id} : {e}")
            return []

    def add_user(self, user_name):
        """
        Query to check if user already exist and also to add user .
        """
        try:
            with self.app.app_context():
                user = User.query.filter_by(user_name = user_name).first()
                if user :
                    return None # User already exists, return the existing user

                new_user = User(user_name = user_name,)
                db.session.add(new_user)
                db.session.commit()
                return new_user # Return the newly created user

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Data base error to add user: {e}")
            return None # Return None in case of an error

    def add_movie(self, user_id, movie_name, movie_director,
                  movie_year, movie_rating, movie_poster):
        """
        Query to check if movie already exist . if not ,
        then add new movie details to the db.
        """
        try:
            with self.app.app_context():
                movie = Movie.query.filter_by(movie_name = movie_name).first()
                if movie:
                    return None  # Movie already exists, return the existing user

                new_movie = Movie(
                movie_name = movie_name,
                movie_director = movie_director,
                movie_year = movie_year,
                movie_rating = movie_rating,
                movie_poster = movie_poster,
                user_id = user_id
                )
                db.session.add(new_movie)
                db.session.commit()
                return new_movie  # Return the newly added movie

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Data base error to add user: {e}")
            return None

    def update_movie(self, user_id, movie_id,movie_name,
                     movie_director,movie_year,movie_rating):
        """
        Query to update the movie details into the db
        """
        try:
            with self.app.app_context():
                movie = Movie.query.filter(Movie.movie_id == movie_id).first()
                if movie:
                    movie.movie_name = movie_name
                    movie.movie_director = movie_director
                    movie.movie_year = movie_year
                    movie.movie_rating = movie_rating
                    db.session.commit()
                    return movie

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Data base error to add user: {e}")
            return None

    def delete_movie(self, user_id, movie_id):
        """
        Query to delete a movie from the database.
        """
        with self.app.app_context():
            movie = Movie.query.filter(Movie.movie_id == movie_id).first()
            if movie:
                db.session.delete(movie)
                db.session.commit()  # Commit the deletion

    def best_movies(self):
        """
        Query to choose the best movie based on the rating from the database.
        """
        with self.app.app_context():
            movies = Movie.query.order_by(Movie.movie_rating.desc()).limit(5).all()
        return movies