from fastapi import APIRouter, Depends

from db import get_session
from db.actions import create_question_set, create_question
from models.question import CreateQuestion
from security import verify_password, manager

router = APIRouter()

@router.post("/create")
async def create(
    question_set: CreateQuestion, active_user=Depends(manager), db=Depends(get_session)
):
    qs = create_question_set(user_id=active_user.id, title=question_set.title, description=question_set.description, db=db)

    for question in question_set.questions:
        create_question(question_set_id=qs.id,
                        text=question["text"],
                        choice1=question["choice1"],
                        choice2=question["choice2"],
                        choice3=question["choice3"],
                        choice4=question["choice4"], db=db)

    return qs.id