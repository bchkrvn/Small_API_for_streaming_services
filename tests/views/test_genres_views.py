class TestGenresView:

    def test_many(self, client, genre_1, headers):
        response = client.get("/genres/", headers=headers)
        assert response.status_code == 200
        assert response.json == [{"id": genre_1.id, "name": genre_1.name}]

    def test_genre_pages(self, client, genre_1, headers):
        response = client.get("/genres/?page=1", headers=headers)
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/genres/?page=2", headers=headers)
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_genre(self, client, genre_1, headers):
        response = client.get("/genres/1/", headers=headers)
        assert response.status_code == 200
        assert response.json == {"id": genre_1.id, "name": genre_1.name}

    def test_genre_not_found(self, client, genre_1, headers):
        response = client.get("/genres/2/", headers=headers)
        assert response.status_code == 404
