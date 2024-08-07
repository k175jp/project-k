import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.user import router as user_router
from routes.question import router as question_router

from secret import create_secret
from db import create_tables
create_secret()
create_tables()

app = FastAPI()

origins = os.getenv("ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")
app.include_router(question_router, prefix="/question")
