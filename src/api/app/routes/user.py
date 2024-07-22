from db import get_session
from db.actions import create_user, get_user_by_name
from exceptions import InvalidPermissions, InvalidUserName, UsernameAlreadyTaken
from models.user import UserCreate, UserResponse
from security import manager
from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=201)
async def register(user: UserCreate, db=Depends(get_session)) -> UserResponse:
    try:
        user = create_user(user.username, user.password, db)
        return UserResponse.from_orm(user)
    except IntegrityError:
        raise UsernameAlreadyTaken


@router.get("/")
async def read_user(
    active_user=Depends(manager), db=Depends(get_session)
) -> UserResponse:
    return