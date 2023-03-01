from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        """
        Получить фильм по его id
        :param pk: id фильма
        :return: Movie
        """
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> list[Movie]:
        """
        Получить все фильма
        :param page: номер страницы
        :param status: сортировать ли по году
        :return: list[Movie]
        """
        return self.dao.get_all(page=page, status=status)
