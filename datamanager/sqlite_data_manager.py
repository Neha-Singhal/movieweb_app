from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datamanager.data_manager_interface import DataManagerInterface
from models import User, Movie  # Import your models

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.engine = create_engine(f'sqlite:///{db_file_name}')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        def get_all_users(self):
            return self.session.query(User).all()

        def get_user_movies(self, user_id):
            return self.session.query(Movie).filter_by(user_id=user_id).all()

        def add_user(self, name):
            user = User(name=name)
            self.session.add(user)
            self.session.commit()
            return user

        def add_movie(self, user_id, name, director, year, rating):
            movie = Movie(name=name, director=director, year=year, rating=rating, user_id=user_id)
            self.session.add(movie)
            self.session.commit()
            return movie

        def update_movie(self, movie_id, name=None, director=None, year=None, rating=None):
            movie = self.session.query(Movie).get(movie_id)
            if movie:
                if name:
                    movie.name = name
                if director:
                    movie.director = director
                if year:
                    movie.year = year
                if rating:
                    movie.rating = rating
                self.session.commit()
            return movie

        def delete_movie(self, movie_id):
            movie = self.session.query(Movie).get(movie_id)
            if movie:
                self.session.delete(movie)
                self.session.commit()
            return movie

        def close(self):
            self.session.close()