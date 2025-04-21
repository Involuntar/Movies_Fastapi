from pydantic import BaseModel, Field
from datetime import datetime as dt
from datetime import date

class CreateGenre(BaseModel):
    genre_name:str=Field(example='Триллер')
    genre_description:str|None=Field(example="Фильм-катастрофа")

class CreateMovie(BaseModel):
    movie_name:str=Field(example="Земля")
    year:int=Field(ge=1900, le=3000, example="2009")
    time:int=Field(gt=0, example=106)
    rate:float=Field(ge=0, le=10, example=6)
    description:str|None=Field(example="Фильм-катастрофа")
    poster:str=Field(example="/ссылка")
    add_date:date=Field(exmaple="2012-12-12")
