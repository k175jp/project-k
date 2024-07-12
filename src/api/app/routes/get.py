from fastapi import APIRouter, Depends

from db import get_session
from security import verify_password
from db.actions import get_question_set

router = APIRouter()

@router.post("/question_set")
async def read_question_set(
    user_id, active_user=Depends(manager), db=Depends(get_session)
):
question_set = actions.get_question_set(user_id, db)

return UserResponse.from_orm(user).model_dump()
