import pytest

from project.models import Movie


class TestGenresView:
    @pytest.fixture
    def movie_1(self, db):
        obj = Movie(
            title='test_title_1',
            description='test_description_1',
            trailer='test_trailer_1',
            year=1,
            rating=1.1,
            genre_id=1,
            director_id=2,
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    @pytest.fixture
    def movie_2(self, db):
        obj = Movie(
            title='test_title_2',
            description='test_description_2',
            trailer='test_trailer_2',
            year=2,
            rating=2.2,
            genre_id=2,
            director_id=2,
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie_1, movie_2, headers):
        response = client.get("/movies/", headers=headers)
        assert response.status_code == 200
        assert response.json == [
            {
                'id': movie_1.id,
                'title': movie_1.title,
                'description': movie_1.description,
                'trailer': movie_1.trailer,
                'year': movie_1.year,
                'rating': movie_1.rating,
                'genre_id': movie_1.genre_id,
                'director_id': movie_1.director_id,
            },
            {
                'id': movie_2.id,
                'title': movie_2.title,
                'description': movie_2.description,
                'trailer': movie_2.trailer,
                'year': movie_2.year,
                'rating': movie_2.rating,
                'genre_id': movie_2.genre_id,
                'director_id': movie_2.director_id,
            }
        ]

    def test_movies_pages(self, app, client, movie_1, movie_2, headers):
        app.config['ITEMS_PER_PAGE'] = 1
        response = client.get("/movies/?page=1", headers=headers)
        assert response.status_code == 200
        assert response.json == [{
                'id': movie_1.id,
                'title': movie_1.title,
                'description': movie_1.description,
                'trailer': movie_1.trailer,
                'year': movie_1.year,
                'rating': movie_1.rating,
                'genre_id': movie_1.genre_id,
                'director_id': movie_1.director_id,
            }]
        assert len(response.json) == 1

        response = client.get("/movies/?page=2", headers=headers)
        assert response.status_code == 200
        assert response.json == [{
                'id': movie_2.id,
                'title': movie_2.title,
                'description': movie_2.description,
                'trailer': movie_2.trailer,
                'year': movie_2.year,
                'rating': movie_2.rating,
                'genre_id': movie_2.genre_id,
                'director_id': movie_2.director_id,
            }]
        assert len(response.json) == 1

        response = client.get("/movies/?page=3", headers=headers)
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movies_status(self, client, movie_1, movie_2, headers):
        response = client.get("movies/?status=new", headers=headers)
        assert response.status_code == 200
        assert len(response.json) == 2
        assert response.json[0] == {
                'id': movie_2.id,
                'title': movie_2.title,
                'description': movie_2.description,
                'trailer': movie_2.trailer,
                'year': movie_2.year,
                'rating': movie_2.rating,
                'genre_id': movie_2.genre_id,
                'director_id': movie_2.director_id,
            }
        assert response.json[1] == {
                'id': movie_1.id,
                'title': movie_1.title,
                'description': movie_1.description,
                'trailer': movie_1.trailer,
                'year': movie_1.year,
                'rating': movie_1.rating,
                'genre_id': movie_1.genre_id,
                'director_id': movie_1.director_id,
            }

    def test_movie(self, client, movie_1, headers):
        response = client.get("/movies/1/", headers=headers)
        assert response.status_code == 200
        assert response.json == {
                'id': movie_1.id,
                'title': movie_1.title,
                'description': movie_1.description,
                'trailer': movie_1.trailer,
                'year': movie_1.year,
                'rating': movie_1.rating,
                'genre_id': movie_1.genre_id,
                'director_id': movie_1.director_id,
            }

    def test_movie_not_found(self, client, movie_1, headers):
        response = client.get("/movies/3/", headers=headers)
        assert response.status_code == 404
