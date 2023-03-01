from flask_restx import Namespace, Resource
from flask import request

from project.container import user_service
from project.helpers.decorators import auth_required, user_required
from project.models import UserSchema

api = Namespace('users')
user_schema = UserSchema()


@api.route('/')
class UserViews(Resource):
    @user_required
    def get(self, user_email=None):
        user = user_service.get_by_email(user_email)
        return user_schema.dump(user), 200

    @user_required
    def patch(self, user_email=None):
        user_data = request.json
        user_data['email'] = user_email
        user_service.update_partial(user_data)
        return '', 204


@api.route('/password')
class UserPasswordViews(Resource):
    @user_required
    def put(self, user_email=None):
        user_data = request.json
        user_data['email'] = user_email
        user_service.change_password(user_data)

        return '', 204


