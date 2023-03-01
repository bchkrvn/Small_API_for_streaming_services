from flask import abort

from project.dao.main import UserMoviesDAO
from project.models import UserMovies
from project.services.movies_service import MoviesService
from project.services.user_service import UsersService


class UserMoviesService:
    def __init__(self, user_movies_dao: UserMoviesDAO, user_service=UsersService, movies_service=MoviesService) -> None:
        self.user_movies_dao = user_movies_dao
        self.user_service = user_service
        self.movies_service = movies_service

    def add_to_favorites(self, movie_id: int, user_email: str):
        """
        Добавляет фильм в список избранных для пользователя
        :param movie_id: id фильма
        :param user_email: email пользователя
        """
        user = self.user_service.get_by_email(email=user_email)
        movie = self.movies_service.get_item(pk=movie_id)

        # Проверка есть ли уже в избранном
        if self.user_movies_dao.is_favorite(movie, user):
            abort(400)

        new_favorite = UserMovies(user=user, movie=movie)
        self.user_movies_dao.add_to_favorites(new_favorite)

    def delete_from_favorites(self, movie_id: int, user_email: str):
        """
        Удаляет фильм из избранных у пользователя
        :param movie_id: id фильма
        :param user_email: email пользователя
        :return:
        """
        user = self.user_service.get_by_email(email=user_email)
        movie = self.movies_service.get_item(pk=movie_id)
        favorite = self.user_movies_dao.get_favorite(movie, user)

        # Проверка есть ли в избранном
        if not favorite:
            abort(400)

        self.user_movies_dao.delete_from_favorites(favorite)
