class TestFavoritesViews:
    def test_add_to_favorites(self, client, movie_1, user_1, headers, user_movie_service):
        response = client.post('/favorites/movies/1', headers=headers)
        assert response.status_code == 201

        favorite = user_movie_service.get_all()[0]
        assert favorite.user_id == user_1.id
        assert favorite.movie_id == movie_1.id

    def test_add_to_favorites_wrong(self, client, movie_1, user_1, favorite_1, user_movie_service, headers):
        # Уже в избранном
        response_1 = client.post('/favorites/movies/1', headers=headers)
        assert response_1.status_code == 400

        # Добавление несуществующего фильма
        response_2 = client.post('/favorites/movies/10000', headers=headers)
        assert response_2.status_code == 404

    def test_delete_from_favorites(self, client, favorite_1, favorite_2, movie_2, user_2, user_movie_service, headers):
        response = client.delete('/favorites/movies/1', headers=headers)
        assert response.status_code == 204

        favorites = user_movie_service.get_all()
        assert type(favorites) is list
        assert len(favorites) == 1
        assert favorites[0].user_id == user_2.id
        assert favorites[0].movie_id == movie_2.id

    def test_delete_from_favorites_wrong(self, client, favorite_1, movie_1, user_1, user_2,
                                         movie_2, user_movie_service, headers):
        # Фильм не в избранном
        response = client.delete('/favorites/movies/2', headers=headers)
        assert response.status_code == 400
