from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.sqlite import DATE, TIME
from db import Base


class MovieModel(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return f"[{self.movie_id}] - {self.name} ({self.rating})"


class ProjectionModel(Base):
    __tablename__ = "projections"
    projection_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'))
    projection_type = Column(String)
    projection_date = Column(String)
    projection_time = Column(String)
    movie = relationship('MovieModel')


class ReservarionModel(Base):
    __tablename__ = 'reservations'
    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    projection_id = Column(Integer, ForeignKey('projections.projection_id'))
    row = Column(Integer)
    col = Column(Integer)
    user = relationship('UserModel', backref='reservations')
    projection = relationship('ProjectionModel')
