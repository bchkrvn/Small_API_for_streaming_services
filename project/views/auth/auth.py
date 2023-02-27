from flask_restx import Namespace, Resource
from flask import request, abort

from project.container import auth_service, user_service

api = Namespace('auth')


@api.route('/register')
class AuthRegister(Resource):
    def post(self):
        user_data = request.json

        if ['email', 'password'] != list(user_data.keys()):
            abort(400)

        user_service.create(user_data)

        return "", 201


@api.route('/login')
class AuthLogin(Resource):
    def post(self):
        user_data = request.json
        if ['email', 'password'] != list(user_data.keys()):
            abort(400)

        email = user_data.get('email')
        password = user_data.get('password')

        return auth_service.generate_token(email, password)

    def put(self):
        tokens = request.json

        if 'refresh_token' not in tokens.keys():
            abort(400)

        return auth_service.approve_refresh_token(tokens['refresh_token'])

