from langchain.chat_models import ChatOpenAI

class ChatAgent:
    def __init__(self):
        self.llm=ChatOpenAI(temparature=0.2)

    def run(self, message:str) -> str:
        return self.llm.predict(message)
            