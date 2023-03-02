from copy import copy

import pytest

from project.exceptions import ItemNotFound
from project.tools.security import generate_password_hash


class TestUsersService:

    def test_get_user(self, users_service, user_1):
        assert users_service.get_item(user_1.id)

    def test_genre_not_found(self, users_service):
        with pytest.raises(ItemNotFound):
            users_service.get_item(2)

    def test_get_by_email(self, user_1, users_service):
        user_get = users_service.get_by_email(user_1.email)
        assert user_get == user_1

    def test_create_user(self, users_service):
        data = {
            'email': 'email',
            'password': 'password'
        }
        password = generate_password_hash(data.get('password'))
        users_service.create(data)

        user = users_service.get_item(1)
        assert user.email == data.get('email')
        assert user.password == password

    def test_update_partial(self, user_1, users_service, genre_1):
        email = copy(user_1.email)
        data = {
            'email': user_1.email,
            'name': 'name',
            'surname': 'surname',
            'favorite_genre_id': 1
        }
        users_service.update_partial(data)
        update_user = users_service.get_item(1)
        assert update_user.email == email
        assert update_user.surname == data.get('surname')
        assert update_user.favorite_genre_id == data.get('favorite_genre_id')

    def test_change_password(self, user_1, users_service):
        old_password = copy(user_1.password)
        user_data = {
            'email': user_1.email,
            'password_1': '1111',
            'password_2': '2222'
        }
        new_password = generate_password_hash(user_data.get('password_2'))
        users_service.change_password(user_data)
        update_user = users_service.get_item(1)
        assert update_user.password != old_password
        assert update_user.password == new_password

    def test_is_user(self, user_1, users_service):
        assert users_service.is_user(user_1.email)
        assert not users_service.is_user('email_20')
