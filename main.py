from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd


app=FastAPI()

# Фильмы
@app.get('/movies', response_model=List[pyd.BaseMovie])
def get_all_movies(db:Session=Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies

@app.get("/movies/{id}", response_model=pyd.BaseMovie)
def get_movie(id:int, db:Session=Depends(get_db)):
    movie = db.query(m.Movie).filter(
        m.Movie.id==id
    ).first()
    if not movie:
        raise HTTPException(404, 'Фильм не найден')
    return movie

@app.post("/movies", response_model=pyd.BaseMovie)
def create_movie(movie:pyd.CreateMovie, db:Session=Depends(get_db)):
    movie_db = m.Movie()
    movie_db.movie_name = movie.movie_name
    movie_db.year = movie.year
    movie_db.time = movie.time
    movie_db.rate = movie.rate
    movie_db.description = movie.description
    movie_db.poster = movie.poster
    movie_db.add_date = movie.add_date

    db.add(movie_db)
    db.commit()
    return movie_db

@app.put("/movies/{id}", response_model=pyd.CreateMovie)
def update_movie(id:int, movie:pyd.CreateMovie, db:Session=Depends(get_db)):
    movie_db = db.query(m.Movie).filter(
        m.Movie.id==id
    ).first()
    movie_db.movie_name = movie.movie_name
    movie_db.year = movie.year
    movie_db.time = movie.time
    movie_db.rate = movie.rate
    movie_db.description = movie.description
    movie_db.poster = movie.poster
    movie_db.add_date = movie.add_date

    db.add(movie_db)
    db.commit()
    return movie_db

@app.delete("/movies/{id}")
def delete_movie(id:int, db:Session=Depends(get_db)):
    movie = db.query(m.Movie).filter(
        m.Movie.id==id
    ).first()
    if not movie:
        raise HTTPException(404, 'Фильм не найден')
    db.delete(movie)
    db.commit()
    return {'detail': "Фильм удалён"}

# Жанры
@app.get('/genres', response_model=List[pyd.BaseGenre])
def get_all_genres(db:Session=Depends(get_db)):
    genres = db.query(m.Genre).all()
    return genres

@app.post("/genres", response_model=pyd.CreateGenre)
def create_genre(genre:pyd.CreateGenre, db:Session=Depends(get_db)):
    genre_db = m.Genre()
    genre_db.genre_name = genre.genre_name
    genre_db.genre_description = genre.genre_description

    db.add(genre_db)
    db.commit()
    return genre_db
