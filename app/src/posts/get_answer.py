from revChatGPT.V1 import Chatbot
from app.src.posts.schemas import Question


def get_answer(chatbot: Chatbot, question: Question) -> str:
    for response in chatbot.ask(question):
        data = response["message"]
    return data
