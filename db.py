# import sqlite3

# from settings import DB_NAME


# class Database:
#     def __init__(self):
#         self.connection = sqlite3.connect(DB_NAME)
#         self.cursor = self.connection.cursor()

#     def close(self):
#         self.connection.close()


# instance = Database()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cinema.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
