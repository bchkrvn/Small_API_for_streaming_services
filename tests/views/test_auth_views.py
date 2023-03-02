class TestAuthView:
    def test_register(self, client, users_service):
        data = {
            "email": "email",
            "password": "password"
        }
        response_2 = client.post("/auth/register/", json=data)
        assert response_2.status_code == 201

        user = users_service.get_item(1)
        assert user.email == data.get('email')

    def test_wrong_register(self, client, user_1):
        data_1 = dict()
        response_1 = client.post("/auth/register/", json=data_1)
        assert response_1.status_code == 400

        data_2 = {
            "email": user_1.email,
            "password": "password"
        }
        response_2 = client.post("/auth/register/", json=data_2)
        assert response_2.status_code == 400

    def test_login(self, client, user_1):
        data_1 = {
            "email": user_1.email,
            "password": "1111"
        }
        response_1 = client.post("/auth/login/", json=data_1)
        assert response_1.status_code == 200

        tokens = response_1.json
        assert ['access_token', 'refresh_token'] == list(tokens.keys())
        assert tokens['access_token'] is not None
        assert tokens['refresh_token'] is not None

    def test_wrong_login(self, client, user_1):
        # Нет email или password
        data_1 = dict()
        response_1 = client.post("/auth/login/", json=data_1)
        assert response_1.status_code == 400

        # Неправильный пароль
        data_2 = {
            "email": user_1.email,
            "password": "2222"
        }
        response_2 = client.post("/auth/login/", json=data_2)
        assert response_2.status_code == 403

        # Несуществующий пользователь
        data_3 = {
            "email": 'email_3',
            "password": "1111"
        }
        response_3 = client.post("/auth/login/", json=data_3)
        assert response_3.status_code == 404

    def test_update_tokens(self, client, user_1):
        data = {
            "email": user_1.email,
            "password": "1111"
        }
        response_1 = client.post("/auth/login/", json=data)
        assert response_1.status_code == 200

        tokens = response_1.json
        response_2 = client.put("/auth/login/", json=tokens)
        assert response_2.status_code == 200

        tokens = response_2.json
        assert ['access_token', 'refresh_token'] == list(tokens.keys())
        assert tokens['access_token'] is not None
        assert tokens['refresh_token'] is not None

    def test_update_tokens_wrong(self, client, user_1):
        # Отсутствие refresh_token
        tokens_1 = dict()
        response_1 = client.put("/auth/login/", json=tokens_1)
        assert response_1.status_code == 400

        # Неверный refresh_token
        tokens_2 = {
            "refresh_token": "qqqqq.qqqqq.qqqqq"
        }
        response_2 = client.put("/auth/login/", json=tokens_2)
        assert response_2.status_code == 400


