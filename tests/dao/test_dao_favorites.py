from project.models import UserMovies


class TestUsersDAO:

    def test_get_all_favorite(self, favorite_1, favorite_2, users_movies_dao):
        favorite_get = users_movies_dao.get_all()
        assert favorite_get == [favorite_1, favorite_2]

    def test_get_favorite_by_id(self, favorite_1, users_movies_dao):
        favorite_get = users_movies_dao.get_by_id(1)
        assert favorite_get == favorite_1

    def test_get_favorite(self, movie_1, user_1, users_movies_dao, favorite_1):
        get_favorite = users_movies_dao.get_favorite(movie_1, user_1)
        assert get_favorite == favorite_1

    def test_is_favorite(self, user_1, movie_1, movie_3, favorite_1, users_movies_dao):
        assert users_movies_dao.is_favorite(movie_1, user_1)
        assert not users_movies_dao.is_favorite(movie_3, user_1)

    def test_add_to_favorites(self, user_1, movie_3, users_movies_dao):
        new_favorite = UserMovies(user_id=user_1.id, movie_id=movie_3.id)
        users_movies_dao.add_to_favorites(new_favorite)
        last_favorite = users_movies_dao.get_all()[-1]
        assert last_favorite == new_favorite

    def test_delete_from_favorite(self, favorite_1, users_movies_dao):
        users_movies_dao.delete_from_favorites(favorite_1)
        all_favorites = users_movies_dao.get_all()
        assert favorite_1 not in all_favorites
