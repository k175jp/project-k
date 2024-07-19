import random

from fastapi import APIRouter, Depends

from db import get_session
from db.actions import create_question_set, create_question, get_mistakes_question_set, get_question_set_by_id, get_question_set, get_answer, save_result, get_question_set, random_question_set
from models.question import CreateQuestion, QuestionSetResponse, AnswerRequest, GetQuestion
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
    question_set_id: int, mistakes: str = "false", active_user=Depends(manager), db=Depends(get_session)
):
    if mistakes == "true":
        question_set = get_mistakes_question_set(active_user.id, question_set_id, db)
    else:
        question_set = get_question_set_by_id(question_set_id, db)
    for q in question_set:
        qs = [q.choice1, q.choice2, q.choice3, q.choice4]
        rqs = random.sample(qs, len(qs))
        q.choice1 = rqs[0]
        q.choice2 = rqs[1]
        q.choice3 = rqs[2]
        q.choice4 = rqs[3]

    return [QuestionSetResponse.from_orm(q) for q in question_set]

@router.post("/answer")
async def answer(
    answer_request: AnswerRequest, active_user=Depends(manager), db=Depends(get_session)
):
    choice = answer_request.choice
    question_set_id = answer_request.question_set_id
    question_id = answer_request.question_id
    answer = get_answer(question_id ,db)
    user_id = active_user.id
    is_correct = True if choice == answer else False
    save_result(user_id, question_set_id, question_id, is_correct, db)

    return answer

@router.get("/get")
async def read_question_set(
    active_user=Depends(manager), db=Depends(get_session)
):
    question_set = random_question_set(db)

    return [GetQuestion.from_orm(i) for i in question_set]
