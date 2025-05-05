from database import Base
from sqlalchemy import Column, Integer, String, Float, Text, Date, ForeignKey
from sqlalchemy.orm import relationship

class Genre(Base):
    __tablename__="genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String(20), unique=True)
    genre_description = Column(String(255), nullable=True)

class Movie(Base):
    __tablename__="movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_name = Column(String(255))
    year = Column(Integer)
    time = Column(Integer)
    rate = Column(Float)
    description = Column(Text, nullable=True)
    poster = Column(String)
    add_date = Column(Date)
    
    genres = relationship("Genre", secondary="genre_movies", backref="movies")

class Genre_Movie(Base):
    __tablename__="genre_movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=True)

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)