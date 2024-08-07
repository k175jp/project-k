from typing import Optional

from db import SessionLocal
from db.models import User, QuestionSet, Question, Result
from security import hash_password, manager
from sqlalchemy import asc, or_
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

def create_question_set(user_id: int, title, description, db: Session) -> QuestionSet:
    question_set = QuestionSet(user_id=user_id, title=title, description=description)
    db.add(question_set)
    db.commit()
    return question_set

def create_question(question_set_id: int, text: str, choice1: str, choice2: str, choice3: str, choice4: str, db: Session) -> Question:
    question = Question(question_set_id=question_set_id, text=text, choice1=choice1, choice2=choice2, choice3=choice3, choice4=choice4)
    db.add(question)
    db.commit()
    return question

def get_mistakes_question_set(user_id: int, question_set_id: int, db: Session) -> QuestionSet:
    question_set_all = db.query(Result).where(Result.question_set_id == question_set_id, Result.user_id == user_id, Result.is_correct == False).all()
    question_ids = []
    for question in question_set_all:
        question_ids.append(question.question_id)
    question_set = db.query(Question).where(Question.id.in_(question_ids)).order_by(asc(Question.id))
    return question_set

def get_question_set_by_id(question_set_id: int, db: Session) -> QuestionSet:
    question_set = db.query(Question).where(Question.question_set_id == question_set_id).order_by(asc(Question.id)).all()
    return question_set

def get_answer(question_id: int, db: Session) -> str:
    answer = db.query(Question).where(Question.id == question_id).first()
    return answer.choice1

def save_result(user_id: int, question_set_id: int, question_id: int, is_correct: bool, db: Session):
    before = db.query(Result).where(Result.user_id == user_id, Result.question_id == question_id).first()
    if before:
        before.is_correct = is_correct
    else:
        result = Result(user_id=user_id, question_set_id=question_set_id, question_id=question_id, is_correct=is_correct)
        db.add(result)
    db.commit()

def get_question_set(db: Session):
    question = db.query(QuestionSet.title, QuestionSet.description, QuestionSet.id, User.username.label("username")).join(User, User.id == QuestionSet.user_id).all()
    return question

def search_keyword(keyword: str, db: Session):
    question_set = db.query(QuestionSet.title, QuestionSet.description, QuestionSet.id, User.username.label("username")).where(or_(QuestionSet.title.like(f'%{keyword}%'), QuestionSet.description.like(f'%{keyword}%'))).join(User, User.id == QuestionSet.user_id).all()
    return question_set

def search_keyword_me(keyword: str, user_id: int, db: Session):
    question_set = db.query(QuestionSet.title, QuestionSet.description, QuestionSet.id, User.username.label("username")).where(QuestionSet.user_id == user_id, or_(QuestionSet.title.like(f'%{keyword}%'), QuestionSet.description.like(f'%{keyword}%'))).join(User, User.id == QuestionSet.user_id).all()
    return question_set

def my_question_set(user_id: int, db: Session):
    question_set = db.query(QuestionSet.title, QuestionSet.description, QuestionSet.id, User.username.label("username")).where(QuestionSet.user_id == user_id).join(User, User.id == QuestionSet.user_id).all()
    return question_set

def get_result(question_set_id: int, db: Session):
    items = db.query(Result.question_id, Result.is_correct, User.username.label("username")).where(Result.question_set_id == question_set_id).join(User, User.id == Result.user_id).order_by(asc(Result.question_id)).all()
    result = {}
    for item in items:
        if item.username in result.keys():
            result[item.username].append({"question_id": item.question_id, "is_correct": item.is_correct})
        else:
            result[item.username] = [{"question_id": item.question_id, "is_correct": item.is_correct}]
    return result