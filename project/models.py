from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from project.setup.db import db


class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Director(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    genre = relationship('Genre',  foreign_keys=[genre_id])
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)
    director = relationship('Director', foreign_keys=[director_id])


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = relationship('Genre')


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre_id = fields.Int()


class UserMovies(db.Model):
    __tablename__ = 'users_movies'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship('User', foreign_keys=[user_id])
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    movie = relationship('Movie', foreign_keys=[movie_id])


