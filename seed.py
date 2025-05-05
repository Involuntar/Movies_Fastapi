from datetime import datetime as dt
from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    # Фильм 1
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

    # Фильм 2
    movie2 = m.Movie(
        movie_name = "Время",
        year = "2011",
        time = "109",
        rate = "8.4",
        description = "История про будущее, в котором главной и единственной валютой становится драгоценное человеческое время: оно в принципе идет, а если тебе нужна какая-то услуга, ...",
        poster = "/ссылка",
        add_date = dt.strptime("2011-10-27", "%Y-%m-%d").date()
    )
    session.add(movie2)

    genre2 = m.Genre(
        genre_name = "Боевик"
    )
    session.add(genre2)

    genre_movie2 = m.Genre_Movie(
        movie_id = '2',
        genre_id = '2'
    )
    session.add(genre_movie2)

    # Фильм 3
    movie3 = m.Movie(
        movie_name = "Довод",
        year = "2020",
        time = "150",
        rate = "7.5",
        description = "Главный герой — секретный агент, который проходит жестокий тест на надежность и присоединяется к невероятной миссии. От ее выполнения зависит судьба мира, а для успеха необходимо отбросить все прежние представления о пространстве и времени.",
        poster = "/ссылка",
        add_date = dt.strptime("2020-09-03", "%Y-%m-%d").date()
    )
    session.add(movie3)

    genre3 = m.Genre(
        genre_name = "Научная фантастика"
    )
    session.add(genre3)

    genre_movie3 = m.Genre_Movie(
        movie_id = '3',
        genre_id = '2'
    )
    session.add(genre_movie3)

    genre_movie4 = m.Genre_Movie(
        movie_id = '3',
        genre_id = '3'
    )
    session.add(genre_movie4)

    genre_movie5 = m.Genre_Movie(
        movie_id = '2',
        genre_id = '3'
    )
    session.add(genre_movie5)

    user = m.User(
        username = "admin",
        password = "pass"
    )
    session.add(user)

    session.commit()