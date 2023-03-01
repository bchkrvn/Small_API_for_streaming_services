from flask_restx import Namespace, Resource
from flask import request, abort

from project.container import auth_service, user_service

api = Namespace('auth', "Страница для регистрации нового пользователя,"
                        "для его авторизации и обновления токена")


@api.route('/register')
class AuthRegister(Resource):
    def post(self):
        """
        Регистрация нового пользователя
        """
        user_data = request.json
        if ['email', 'password'] != list(user_data.keys()):
            abort(400)
        user_service.create(user_data)

        return "", 201


@api.route('/login')
class AuthLogin(Resource):
    def post(self):
        """
        Авторизация пользователя
        """
        user_data = request.json
        if ['email', 'password'] != list(user_data.keys()):
            abort(400)

        email = user_data.get('email')
        password = user_data.get('password')

        return auth_service.generate_token(email, password)

    def put(self):
        """
        Обновление токена на основе refresh_token
        """
        tokens = request.json

        if 'refresh_token' not in tokens.keys():
            abort(400)

        return auth_service.approve_refresh_token(tokens['refresh_token'])

