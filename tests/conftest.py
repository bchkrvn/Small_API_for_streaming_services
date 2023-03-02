import pytest

from project.config import TestingConfig
from project.server import create_app
from project.setup.db import db as database


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client


@pytest.fixture
def headers():
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5pa2l0YSIsImV4cCI6MTY4ODk3MTQzMH0.-2rr8484beZ8NESao1M6yPzxCLaQXYA--Cj2B5u5Bp0'}
    return headers
