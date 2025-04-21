from datetime import datetime as dt
from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    movie1 = m.Movie(
        movie_name = "Знамение",
        year = "2009",
        time = "106",
        rate = "6",
        description = "Фильм-катастрофа",
        poster = "/ссылка",
        add_date = dt.strptime("2012-12-12", "%Y-%m-%d").date()
    )
    session.add(movie1)

    genre1 = m.Genre(
        genre_name = "Триллер"
    )
    session.add(genre1)

    genre_movie1 = m.Genre_Movie(
        movie_id = '1',
        genre_id = '1'
    )
    session.add(genre_movie1)

    session.commit()