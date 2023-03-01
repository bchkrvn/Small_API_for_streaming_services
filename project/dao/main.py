from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User, UserMovies


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page=None, status=None):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if status == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_by_email(self, email: str):
        return self._db_session.query(self.__model__).filter(self.__model__.email == email).first()

    def save(self, user: User):
        self._db_session.add(user)
        self._db_session.commit()


class UserMoviesDAO(BaseDAO[UserMovies]):
    __model__ = UserMovies

    def get_favorite(self, movie: Movie, user: User):
        return self._db_session.query(self.__model__).filter(self.__model__.user == user,
                                                             self.__model__.movie == movie).first()

    def is_favorite(self, movie: Movie, user: User):
        return bool(self._db_session.query(self.__model__).filter(self.__model__.user == user,
                                                                  self.__model__.movie == movie).first())

    def add_to_favorites(self, new_favorite: UserMovies):
        self._db_session.add(new_favorite)
        self._db_session.commit()

    def delete_from_favorites(self, favorites: UserMovies):
        self._db_session.delete(favorites)
        self._db_session.commit()
