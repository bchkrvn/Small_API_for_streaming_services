from copy import copy

from project.tools.security import generate_password_hash


class TestUserView:
    def test_get_user(self, user_1, client, headers):
        response = client.get("/users/", headers=headers)
        assert response.status_code == 200
        assert response.json == {
            'id': user_1.id,
            'email': user_1.email,
            'name': user_1.name,
            'surname': user_1.surname,
            'favorite_genre_id': user_1.favorite_genre_id,
        }

    def test_patch(self, user_1, client, headers, genre_1, genre_2):
        old_name = copy(user_1.name)
        old_surname = copy(user_1.surname)
        old_favorite_genre_id = copy(user_1.favorite_genre_id)
        new_data = {
            "name": "name_2",
            "surname": "surname_2",
            "favorite_genre_id": 2
        }
        response_1 = client.patch("/users/", json=new_data, headers=headers)
        assert response_1.status_code == 204

        response_2 = client.get("/users/", headers=headers)
        assert response_2.status_code == 200
        user = response_2.json

        assert user['name'] != old_name
        assert user['name'] == new_data.get('name')
        assert user['surname'] != old_surname
        assert user['surname'] == new_data.get('surname')
        assert user['favorite_genre_id'] != old_favorite_genre_id
        assert user['favorite_genre_id'] == new_data.get('favorite_genre_id')

    def test_password(self, user_1, client, headers):
        data = {
            "password_1": "1111",
            "password_2": "2222"
        }
        data_hash = {
            "password_1": generate_password_hash(data.get("password_1")),
            "password_2": generate_password_hash(data.get("password_2"))
        }
        response_1 = client.put("/users/password", json=data, headers=headers)
        assert response_1.status_code == 204

        assert user_1.password != data_hash.get('password_1')
        assert user_1.password == data_hash.get('password_2')
