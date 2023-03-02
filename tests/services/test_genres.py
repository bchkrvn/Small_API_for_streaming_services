import pytest

from project.exceptions import ItemNotFound


class TestGenresService:
    def test_get_genre(self, genres_service, genre_1):
        assert genres_service.get_item(genre_1.id)

    def test_genre_not_found(self, genres_dao, genres_service):
        with pytest.raises(ItemNotFound):
            genres_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_genres(self, genres_dao, genres_service, page, genre_1, genre_2):
        genres = genres_service.get_all(page=page)
        assert len(genres) == 2
        assert genres == [genre_1, genre_2]
        genres_dao.get_all(page=page)
