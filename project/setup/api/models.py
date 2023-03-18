from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тейлор Шеридан')
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=200, example='Йеллоустоун'),
    'description': fields.String(required=True, max_length=255,
                                 example='Владелец ранчо пытается сохранить землю своих предков. '
                                         'Кевин Костнер в неовестерне от автора «Ветреной реки»'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=UKei_d0cbP4'),
    'year': fields.Integer(required=True, example=2018),
    'rating': fields.Float(required=True, example=8.6),
    'genre_id': fields.Integer(required=True, example=17),
    'genre': fields.Nested(genre),
    'director_id': fields.Integer(required=True, example=1),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(requred=True, example='mail@mail.ru'),
    'password': fields.String(requred=True, example='1234'),
    'name': fields.String(requred=True, example='Name'),
    'surname': fields.String(requred=True, example="Surname"),
    'favorite_genre_id': fields.Integer(requred=True, example=1),
    'genre': fields.Nested(genre)
})
