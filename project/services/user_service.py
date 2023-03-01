from flask import abort
from project.dao.main import UserDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash, compose_passwords


class UsersService:
    def __init__(self, dao: UserDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_by_email(self, email: str) -> User:
        if user := self.dao.get_by_email(email):
            return user
        raise ItemNotFound(f'User with email={email} not exists.')

    def create(self, data):
        data['password'] = generate_password_hash(data.get('password'))
        new_user = User(**data)
        self.dao.save(new_user)

    def update_partial(self, data):
        user = self.get_by_email(data['email'])

        if 'password' in data:
            user.password = data.get('password')
        if 'name' in data:
            user.name = data.get('name')
        if 'surname' in data:
            user.surname = data.get('surname')
        if 'favorite_genre_id' in data:
            user.favorite_genre_id = data.get('favorite_genre_id')
        self.dao.save(user)

    def change_password(self, user_data):
        user = self.get_by_email(user_data['email'])
        password = user_data['password_1']

        if compose_passwords(user.password, password):
            print(1)
            new_password = generate_password_hash(user_data['password_2'])
            user.password = new_password
            self.dao.save(user)
        else:
            return abort(403)

