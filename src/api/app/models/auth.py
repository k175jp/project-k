from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AuthRequest(BaseModel):
    username: str
    password: str