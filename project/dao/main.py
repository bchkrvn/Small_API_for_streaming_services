from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Genre]):
    __model__ = Director


class MoviesDAO(BaseDAO[Genre]):
    __model__ = Movie
