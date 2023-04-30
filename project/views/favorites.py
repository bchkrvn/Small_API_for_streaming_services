from flask_restx import Namespace, Resource

from project.container import user_movie_service
from project.helpers.decorators import user_required
from project.setup.api.models import movie
from project.container import movie_service

favorite_ns = Namespace('favorites', "Страница для добавления фильма в избранные")


@favorite_ns.route('/movies/')
class FavoritesView(Resource):
    @favorite_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    @user_required
    def get(self, user_email):
        likes = user_movie_service.get_all_user(user_email)
        movies = []
        for like in likes:
            movie = movie_service.get_item(like.movie_id)
            movies.append(movie)
        return movies


@favorite_ns.route('/movies/<int:movie_id>')
class FavoritesViews(Resource):
    @user_required
    def post(self, movie_id: int, user_email=None):
        """
        Добавление фильма в избранные
        :param movie_id: id фильма
        :param user_email: email пользователя из токена
        """
        user_movie_service.add_to_favorites(movie_id, user_email)
        return '', 201

    @user_required
    def delete(self, movie_id: int, user_email=None):
        """
        Удалить фильм из избранного
        :param movie_id: id фильма
        :param user_email: email пользователя из токена
        """
        user_movie_service.delete_from_favorites(movie_id, user_email)
        return '', 204
