from fastapi import fastapi
from app.api.routes_chat import router as chat_router
from app.api.health import router as health_router

app = fastapi(title="AI Agent Platform")

app.include_router(chat_router, prefix="/api/chat")
app.include_router(health_router, prefix="/health")
