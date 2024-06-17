from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(80))
    
    question_sets = relationship("QuestionSet", backref="question_set")
    result = relationship("Result", backref="result")

    def __repr__(self) -> str:
        return f"User(username={self.username})"


class QuestionSet(Base):
    __tablename__ == "question_set"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(32))
    description = Column(String(256))
    
    questions = relationship("Question", backref="question")
    result = relationship("Result", backref="result")

    def __repr__(self) -> str:
        return f"QuestionSet(user_id={self.user_id}, title={self.title}, description={self.description})"
    

class Question(Base):
    __tablename__ == "question"
    
    id = Column(Integer, primary_key=True)
    question_set_id = Column(Integer, ForeignKey("question_set.id"))
    text = Column(String(255))
    choice1 = Column(String(255))
    choice2 = Column(String(255))
    choice3 = Column(String(255))
    choice4 = Column(String(255))

    result = relationship("Result", backref="result")

    def __repr__(self) -> str:
        return f"Question(question_set_id={self.question_set_id}, text={self.text}, choice1={self.choice1}, choice2={self.choice2}, choice3={self.choice3}, choice4={self.choice4})"


class Result(Base):
    __tablename__ == "result"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_set_id = Column(Integer, ForeignKey("question_set.id"))
    question_id = Column(Integer, ForeignKey("question.id"))
    is_correct = Column(Boolean)
 
    def __repr__(self) -> str:
        return f"Result(user_id={self.user_id}, question_set_id={self.question_set_id}, question_id={self.question_id}, is_correct={self.is_correct})"