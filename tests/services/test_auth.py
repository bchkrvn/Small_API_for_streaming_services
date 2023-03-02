class TestAuthService:

    def test_generate_token(self, auth_service, user_1):
        tokens = auth_service.generate_token(user_1.email, '1111')

        assert ['access_token', 'refresh_token'] == list(tokens.keys())
        assert tokens['access_token'] is not None
        assert tokens['refresh_token'] is not None

    def test_approve_refresh_token(self, auth_service, user_1):
        tokens = auth_service.generate_token(user_1.email, '1111')
        refresh_token = tokens['refresh_token']
        new_tokens = auth_service.approve_refresh_token(refresh_token)

        assert ['access_token', 'refresh_token'] == list(tokens.keys())
        assert new_tokens['access_token'] is not None
        assert new_tokens['refresh_token'] is not None
