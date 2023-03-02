class TestDirectorView:

    def test_many(self, client, director_1, headers):
        response = client.get("/directors/", headers=headers)
        assert response.status_code == 200
        assert response.json == [{"id": director_1.id, "name": director_1.name}]

    def test_director_pages(self, client, director_1, headers):
        response = client.get("/directors/?page=1", headers=headers)
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/directors/?page=2", headers=headers)
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_director(self, client, director_1, headers):
        response = client.get("/directors/1/", headers=headers)
        assert response.status_code == 200
        assert response.json == {"id": director_1.id, "name": director_1.name}

    def test_genre_not_found(self, client, director_1, headers):
        response = client.get("/directors/2/", headers=headers)
        assert response.status_code == 404
