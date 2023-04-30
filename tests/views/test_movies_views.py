class TestGenresView:
    keys = ['id', 'title', 'description', 'trailer', 'year', 'rating', 'genre_id', 'genre', 'director_id',
            'director']

    def test_many(self, client, movie_1, movie_2, headers):
        response = client.get("/movies/", headers=headers)

        assert response.status_code == 200
        assert type(response.json) is list
        assert len(response.json) == 2
        assert type(response.json[0]) is dict
        assert list(response.json[0].keys()) == self.keys
        assert None not in response.json[0].values()

    def test_movies_pages(self, app, client, movie_1, movie_2, director_1, director_2, genre_1, genre_2, headers):
        app.config['ITEMS_PER_PAGE'] = 1
        response_1 = client.get("/movies/?page=1", headers=headers)

        assert response_1.status_code == 200
        assert type(response_1.json) is list
        assert len(response_1.json) == 1
        assert type(response_1.json[0]) is dict
        assert list(response_1.json[0].keys()) == self.keys
        assert None not in response_1.json[0].values()

        response_2 = client.get("/movies/?page=3", headers=headers)
        assert response_2.status_code == 200
        assert len(response_2.json) == 0

    def test_movies_status(self, client, movie_1, movie_2, headers):
        response = client.get("movies/?status=new", headers=headers)

        assert response.status_code == 200
        assert type(response.json) is list
        assert len(response.json) == 2
        assert type(response.json[0]) is dict
        assert list(response.json[0].keys()) == self.keys
        assert None not in response.json[0].values()

    def test_movie(self, client, movie_1, headers):
        response = client.get("/movies/1/", headers=headers)
        assert response.status_code == 200
        assert type(response.json) is dict
        assert list(response.json.keys()) == self.keys
        assert None not in response.json.values()

    def test_movie_not_found(self, client, movie_1, headers):
        response = client.get("/movies/3/", headers=headers)
        assert response.status_code == 404
