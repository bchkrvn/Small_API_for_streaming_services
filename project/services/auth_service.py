import calendar
import datetime

import jwt
from flask import abort, current_app

from project.services.user_service import UsersService
from project.tools.security import compose_passwords


class AuthService:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False) -> dict:
        """
        Генерация токена для пользователя
        :param email: email пользователя
        :param password: пароль пользователя
        :param is_refresh: обновляется ли токен
        :return: tokens
        """
        user = self.user_service.get_by_email(email)

        if not user:
            abort(400)

        if not is_refresh:
            is_right_password = compose_passwords(user.password, password)

            if not is_right_password:
                abort(403)

        data = {
            'email': user.email,
        }

        # generate access_token
        min_ = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config["TOKEN_EXPIRE_MINUTES"])
        data['exp'] = calendar.timegm(min_.timetuple())
        access_token = jwt.encode(data, current_app.config["JWT_SECRET"], algorithm=current_app.config["JWT_ALGO"])

        # generate refresh_token
        days_ = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config["TOKEN_EXPIRE_DAYS"])
        data['exp'] = calendar.timegm(days_.timetuple())
        refresh_token = jwt.encode(data, current_app.config["JWT_SECRET"], algorithm=current_app.config["JWT_ALGO"])

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

    def approve_refresh_token(self, refresh_token):
        """
        Обновления токена на основе refresh_token
        :param refresh_token: refresh_token
        :return: tokens
        """
        try:
            data = jwt.decode(refresh_token, current_app.config["JWT_SECRET"],
                              algorithms=[current_app.config["JWT_ALGO"]])
            email = data.get('email', None)

        except Exception as e:
            abort(400)

        return self.generate_token(email, None, is_refresh=True)
