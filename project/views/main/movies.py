from flask_restx import Namespace, Resource

from project.container import movie_service
from project.helpers.decorators import auth_required
from project.setup.api.models import movie
from project.setup.api.parsers import movie_page_parser

movies_ns = Namespace('movies', 'Получить информацию о фильмах')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.expect(movie_page_parser)
    @movies_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    # @auth_required
    def get(self):
        """
        Get all movies.
        """
        return movie_service.get_all(**movie_page_parser.parse_args())


@movies_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    @movies_ns.response(404, 'Not Found')
    @movies_ns.marshal_with(movie, code=200, description='OK')
    # @auth_required
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)
