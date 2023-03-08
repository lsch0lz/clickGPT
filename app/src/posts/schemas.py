from pydantic import BaseModel


class Question(BaseModel):
    question: str


class Answer(BaseModel):
    message: str


class Audio(BaseModel):
    encoding: str
