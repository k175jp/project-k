import random

from fastapi import APIRouter, Depends

from db import get_session
from db.actions import create_question_set, create_question, get_question_set_by_id
from models.question import CreateQuestion, QuestionSetResponse
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


@router.get("/get_question_set/{question_set_id}")
async def get_question_set(
    #question_set_id: int, active_user=Depends(manager), db=Depends(get_session)
    question_set_id: int, db=Depends(get_session)
):
    question_set = get_question_set_by_id(question_set_id, db)
    for q in question_set:
        qs = [q.choice1, q.choice2, q.choice3, q.choice4]
        rqs = random.sample(qs, len(qs))
        q.choice1 = rqs[0]
        q.choice2 = rqs[1]
        q.choice3 = rqs[2]
        q.choice4 = rqs[3]
    
    return [QuestionSetResponse.from_orm(q) for q in question_set]

@router.post("answer/{question_set_id}/{question_id}")
async def answer(
    question_set_id: int, question_id: int, active_user=Depends(manager), db=Depends(get_session)
):
    pass