from flask_restx import Namespace, Resource

from project.container import user_movie_service
from project.helpers.decorators import user_required

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies/<int:movie_id>')
class FavoritesViews(Resource):
    @user_required
    def post(self, movie_id: int, user_email=None):
        user_movie_service.add_to_favorites(movie_id, user_email)
        return '', 201

    @user_required
    def delete(self, movie_id: int, user_email=None):
        user_movie_service.delete_from_favorites(movie_id, user_email)
        return '', 204
