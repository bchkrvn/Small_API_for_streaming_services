class TestFavoritesService:

    def test_get_all(self, favorite_1, favorite_2, user_movie_service):
        favorites = user_movie_service.get_all()
        assert type(favorites) is list
        assert len(favorites) == 2
        assert favorites == [favorite_1, favorite_2]

    def test_add_to_favorites(self, movie_1, user_1, user_movie_service):
        user_movie_service.add_to_favorites(movie_1.id, user_1.email)
        favorites = user_movie_service.get_all()[-1]
        assert favorites.user_id == user_1.id
        assert favorites.movie_id == movie_1.id

    def test_delete_from_favorites(self, favorite_1, favorite_2, movie_1, user_1, user_movie_service):
        user_movie_service.delete_from_favorites(movie_1.id, user_1.email)
        favorites = user_movie_service.get_all()

        assert len(favorites) == 1
        assert favorites[0] == favorite_2
