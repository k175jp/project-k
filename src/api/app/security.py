from passlib.context import CryptContext

from fastapi_login import LoginManager

from config import Config

manager = LoginManager(Config.secret, Config.token_url, use_cookie=True)
pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(plaintext: str):
    return pwd_context.hash(plaintext)


def verify_password(plaintext: str, hashed: str):
    return pwd_context.verify(plaintext, hashed)
