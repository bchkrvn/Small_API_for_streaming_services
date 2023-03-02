import pytest

from project.exceptions import ItemNotFound


class TestMoviesService:

    def test_get_movie(self, movies_service, movie_1):
        assert movies_service.get_item(movie_1.id)

    def test_movie_not_found(self, movies_dao, movies_service):
        with pytest.raises(ItemNotFound):
            movies_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_movies(self, movies_dao, movies_service, page, movie_1, movie_2):
        movies = movies_service.get_all(page=page)
        assert len(movies) == 2
        movies_dao.get_all(page=page)
