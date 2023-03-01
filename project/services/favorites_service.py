from typing import Optional
from flask import abort

from project.dao.main import UserMoviesDAO
from project.exceptions import ItemNotFound
from project.models import UserMovies
from project.services.movies_service import MoviesService
from project.services.user_service import UsersService


class UserMoviesService:
    def __init__(self, user_movies_dao: UserMoviesDAO, user_service=UsersService, movies_service=MoviesService) -> None:
        self.user_movies_dao = user_movies_dao
        self.user_service = user_service
        self.movies_service = movies_service

    def add_to_favorites(self, movie_id: int, user_email: str):
        user = self.user_service.get_by_email(email=user_email)
        movie = self.movies_service.get_item(pk=movie_id)

        if self.user_movies_dao.is_favorite(movie, user):
            abort(400)

        new_favorite = UserMovies(user=user, movie=movie)
        self.user_movies_dao.add_to_favorites(new_favorite)

    def delete_from_favorites(self, movie_id: int, user_email: str):
        user = self.user_service.get_by_email(email=user_email)
        movie = self.movies_service.get_item(pk=movie_id)
        favorite = self.user_movies_dao.get_favorite(movie, user)

        if not favorite:
            abort(400)

        self.user_movies_dao.delete_from_favorites(favorite)
