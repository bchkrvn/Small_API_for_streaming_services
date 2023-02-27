from project.dao.main import UserDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash


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


