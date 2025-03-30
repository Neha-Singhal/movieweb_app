from abc import ABC, abstractmethod

class DataManagerInterface(ABC):

    @abstractmethod
    def get_all_users(self):
        """
        Abstract method to get all users.
        """
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """
        Abstract method to get user favourite movies.
        """
        pass

    @abstractmethod
    def get_movie_by_id(self, movie_id):
        """
        Abstract method to movie for the user.
        """
        pass

    @abstractmethod
    def add_user(self,user_name):
        """
        Abstract method to add new user
        """
        pass

    @abstractmethod
    def add_movie(self,user_id, movie_name, movie_director, movie_year,
                  movie_rating,movie_poster):
        """
        Abstract method to add movie for the user
        """
        pass

    @abstractmethod
    def update_movie(self, user_id, movie_id,movie_name,movie_director,
                     movie_year,movie_rating):
        """
        Abstract method to update the movie details of the user
        """
        pass

    @abstractmethod
    def delete_movie(self, user_id, movie_id):
        """
        Abstract method to delete a users movie
        """
        pass

    @abstractmethod
    def best_movies(self):
        """
        Abstract method filter  best movies.
        """
        pass