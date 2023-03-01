import base64
import hashlib
import hmac

from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    """
    Генерация пароля в bytes
    :param password:
    :return:
    """
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    """
    Хеширования пароля в bytes
    :param password: пароль для хеширования
    :return: хахешированый пароль
    """
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compose_passwords(password_hash, password: str) -> bool:
    """
    Сравнение двух паролей в хешированном виде
    :param password_hash: верный пароль
    :param password: пароль, который нужно проверить
    :return: Bool
    """
    decode_digit = base64.b64decode(password_hash)
    other_password_hash = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode('utf-8'),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"]
    )
    return hmac.compare_digest(decode_digit, other_password_hash)
