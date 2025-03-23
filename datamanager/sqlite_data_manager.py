from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datamanager.data_manager_interface import DataManagerInterface
from models import User, Movie  # Import your models

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.engine = create_engine(f'sqlite:///{db_file_name}')
        self.Session = sessionmaker(bind=self.engine)