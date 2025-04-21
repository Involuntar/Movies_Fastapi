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

# # Планеты
# @app.get("/planets", response_model=List[pyd.BasePlanet])
# def get_all_planets(db:Session=Depends(get_db)):
#     planets = db.query(m.Planet).all()
#     return planets

# @app.get("/planet/{planet_id}", response_model=pyd.BasePlanet)
# def get_planet(planet_id:int, db:Session=Depends(get_db)):
#     planet = db.query(m.Planet).filter(
#         m.Planet.id==planet_id
#     ).first()
#     if not planet:
#         raise HTTPException(404, 'Планета не найдена')
#     return planet

# @app.post("/planet", response_model=pyd.BasePlanet)
# def create_planet(planet:pyd.CreatePlanet, db:Session=Depends(get_db)):
#     planet_db = m.Planet()

#     planet_db.planet_name = planet.planet_name
#     planet_db.planet_mass = planet.planet_mass
#     planet_db.planet_diameter = planet.planet_diameter

#     db.add(planet_db)
#     db.commit()
#     return planet_db

# @app.delete("/planet/{planet_id}")
# def delete_product(planet_id:int, db:Session=Depends(get_db)):
#     planet = db.query(m.Planet).filter(
#         m.Planet.id==planet_id
#     ).first()
#     if not planet:
#         raise HTTPException(404, 'Планета не найдена')
#     db.delete(planet)
#     db.commit()
#     return {'detail': "Планета удалена"}
#
