import pytest

from project.exceptions import ItemNotFound


class TestDirectorsService:
    def test_get_director(self, directors_service, director_1):
        assert directors_service.get_item(director_1.id)

    def test_director_not_found(self, directors_dao, directors_service):
        with pytest.raises(ItemNotFound):
            directors_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_directors(self, directors_dao, directors_service, page, director_1, director_2):
        directors = directors_service.get_all(page=page)
        assert len(directors) == 2
        directors_dao.get_all(page=page)
