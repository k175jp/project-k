from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session

from db import get_session
from db.actions import get_user_by_name
from models.auth import Token
from security import verify_password, manager

from datetime import timedelta

router = APIRouter()


@router.post('/login', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    user = get_user_by_name(form_data.username, db)
    if user is None:
        raise InvalidCredentialsException

    if not verify_password(form_data.password, user.password):
        raise InvalidCredentialsException

    token = manager.create_access_token(data={'sub': user.username}, expires=timedelta(hours=12))

    return Token(access_token=token, token_type='bearer')