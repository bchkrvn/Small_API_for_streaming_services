from project.dao import GenresDAO
from project.dao.main import DirectorsDAO, MoviesDAO

from project.services import GenresService
from project.services.directors_service import DirectorsService
from project.services.movies_service import MoviesService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
