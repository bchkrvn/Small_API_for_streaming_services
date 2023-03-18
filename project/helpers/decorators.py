import functools

import jwt
from flask import request, abort, current_app


def user_required(func):
    """
    Проверка кем является пользователь
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            data = jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=[current_app.config["JWT_ALGO"]])
            user_email = data.get('email')
        except Exception as e:
            abort(401)

        return func(*args, **kwargs, user_email=user_email)

    return wrapper


def auth_required(func):
    """
    Проверка - авторизован ли пользователь
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            data = jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=[current_app.config["JWT_ALGO"]])
        except Exception as e:
            abort(401)

        return func(*args, **kwargs)

    return wrapper
