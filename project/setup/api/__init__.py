from flask_restx import Api

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 4",
    description='Инструкция к приложению курсовой работы №4.',
    doc="/docs",
)
