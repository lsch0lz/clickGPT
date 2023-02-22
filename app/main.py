import os
from datetime import timedelta
from revChatGPT.V1 import Chatbot

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.src.auth.authentication import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
    oauth2_scheme,
)
from app.src.auth.config import db, ACCESS_TOKEN_EXPIRE_MINUTES
from app.src.auth.schemas import Token, User
from app.src.posts.schemas import Question, Answer
from app.src.posts.get_answer import get_answer

app = FastAPI()

chatbot = Chatbot(config={"email": str(os.getenv("email")), "password": str(os.getenv("password"))})


@app.post("/clickGPT")
async def ask(question: Question, token: str = Depends(oauth2_scheme)):
    return Answer(message=get_answer(chatbot, question.question))


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
