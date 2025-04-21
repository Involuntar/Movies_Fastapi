from datetime import datetime as dt
from datetime import date
from pydantic import BaseModel, Field

class BaseGenre(BaseModel):
    id:int=Field(example=1)
    genre_name:str=Field(example='Триллер')
    genre_description:str|None=Field(example="Фильм-катастрофа")

class BaseMovie(BaseModel):
    id:int=Field(example=1)
    movie_name:str=Field(example="Знамение")
    year:int=Field(ge=1900, le=3000, example="2009")
    time:int=Field(gt=0, example=106)
    rate:float=Field(ge=0, le=10, example=6)
    description:str|None=Field(example="Фильм-катастрофа")
    poster:str=Field(example="/ссылка")
    add_date:date=Field(example="2012-12-12")
