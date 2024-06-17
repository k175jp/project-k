from db import get_session
from db.actions import create_user, get_user_by_name
from exceptions import InvalidPermissions, InvalidUserName, UsernameAlreadyTaken
from models.user import UserCreate, UserResponse
from security import manager
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/user")


@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserCreate, db=Depends(get_session)) -> UserResponse:
    try:
        user = create_user(user.username, user.password, db)
        return UserResponse.from_orm(user)
    except IntegrityError:
        raise UsernameAlreadyTaken


@router.get("/{username}")
def read_user(
    username, active_user=Depends(manager), db=Depends(get_session)
) -> UserResponse:
    user = get_user_by_name(username, db)

    if user is None:
        raise InvalidUserName

    if user.username != active_user.username:
        raise InvalidPermissions

    return UserResponse.from_orm(user).model_dump()
