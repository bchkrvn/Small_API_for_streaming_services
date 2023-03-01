from project.dao import GenresDAO
from project.dao.main import DirectorsDAO, MoviesDAO, UserDAO

from project.services import GenresService
from project.services.auth_service import AuthService
from project.services.directors_service import DirectorsService
from project.services.movies_service import MoviesService
from project.services.user_service import UsersService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(user_dao=user_dao, genre_dao=genre_dao)
auth_service = AuthService(user_service)
