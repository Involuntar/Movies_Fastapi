from .base_models import *

class SchemeGenreMovie(BaseGenreMovie):
    movie: BaseMovie
    genre: BaseGenre
