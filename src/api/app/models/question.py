from pydantic import BaseModel, ConfigDict
from typing import Dict, List

class CreateQuestion(BaseModel):
    title: str
    description: str
    questions: List[Dict[str, str]]

class QuestionSetResponse(BaseModel):
    id: int
    text: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    model_config = ConfigDict(from_attributes=True)

class AnswerRequest(BaseModel):
    choice: str
    question_set_id: int
    question_id: int