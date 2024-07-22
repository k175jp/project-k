from pydantic import BaseModel
from typing import Dict, List

class CreateQuestion(BaseModel):
    title: str
    description: str
    questions: List[Dict[str, str]]
