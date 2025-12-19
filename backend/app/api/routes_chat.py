from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.agents.chat_agent import ChatAgent 

router = APIRouter()
agent = ChatAgent()

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = agent.run(request.message)
    return ChatResponse(response=reply)
    