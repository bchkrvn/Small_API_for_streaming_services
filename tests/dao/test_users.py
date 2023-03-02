from project.models import User
from project.tools.security import generate_password_hash


class TestUsersDAO:
    def test_get_user_by_id(self, user_1, users_dao):
        assert users_dao.get_by_id(user_1.id) == user_1

    def test_get_user_by_id_not_found(self, users_dao):
        assert not users_dao.get_by_id(1)

    def test_get_user_by_email(self, user_1, users_dao):
        assert users_dao.get_by_email(user_1.email) == user_1

    def test_get_all_genres(self, users_dao, user_1, user_2):
        assert users_dao.get_all() == [user_1, user_2]

    def test_save_user(self, users_dao):
        password = generate_password_hash('3333')
        user_3 = User(email="email_3", password=password)
        users_dao.save(user_3)
        last_user = users_dao.get_all()[-1]
        assert last_user == user_3
