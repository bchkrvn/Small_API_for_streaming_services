from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.models import Movie
from project.services import GenresService


class TestGenresService:

    @pytest.fixture()
    @patch('project.dao.MoviesDAO')
    def movies_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Movie(
            id=1,
            title='test_title_1',
            description='test_description_1',
            trailer='test_trailer_1',
            year=1,
            rating=1.1,
            genre_id=1,
            director_id=2,
        )
        dao.get_all.return_value = [
            Movie(
                id=1,
                title='test_title_1',
                description='test_description_1',
                trailer='test_trailer_1',
                year=1,
                rating=1.1,
                genre_id=1,
                director_id=2,
            ),
            Movie(
                id=2,
                title='test_title_2',
                description='test_description_2',
                trailer='test_trailer_2',
                year=2,
                rating=2.2,
                genre_id=2,
                director_id=2,
            )
        ]
        return dao

    @pytest.fixture()
    def movies_service(self, movies_dao_mock):
        return GenresService(dao=movies_dao_mock)

    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            title='title',
            description='description',
            trailer='trailer',
            year=1,
            rating=1.1,
            genre_id=1,
            director_id=1,
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_movie(self, movies_service, movie):
        assert movies_service.get_item(movie.id)

    def test_movie_not_found(self, movies_dao_mock, movies_service):
        movies_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            movies_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_movies(self, movies_dao_mock, movies_service, page):
        movies = movies_service.get_all(page=page)
        assert len(movies) == 2
        assert movies == movies_dao_mock.get_all.return_value
        movies_dao_mock.get_all.assert_called_with(page=page)
