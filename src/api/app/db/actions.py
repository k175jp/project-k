from typing import Optional

from db import SessionLocal
from db.models import User
from security import hash_password, manager
from sqlalchemy.orm import Session


def get_user_by_name(name: str, db: Session) -> Optional[User]:
    user = db.query(User).where(User.username == name).first()
    return user


@manager.user_loader()
def get_user(name: str):
    with SessionLocal() as db:
        return get_user_by_name(name, db)


def create_user(name: str, password: str, db: Session) -> User:
    hashed_pw = hash_password(password)
    user = User(username=name, password=hashed_pw)
    db.add(user)
    db.commit()
    return user
