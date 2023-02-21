import os
from fastapi import FastAPI
from revChatGPT.V1 import Chatbot

from app.src.posts.schemas import Question, Answer
from app.src.posts.get_answer import get_answer

app = FastAPI()

chatbot = Chatbot(config={
        "email": os.getenv("email"),
        "password": os.getenv("password")
    })

@app.post("/clickGPT")
async def ask(question: Question):
    return Answer(
        message=get_answer(chatbot, question.question)
    )
