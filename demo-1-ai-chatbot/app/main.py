import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .knowledge import find_best_answer, load_knowledge


BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE = load_knowledge(BASE_DIR / "data" / "faqs.json")

app = FastAPI(title="AI Customer Support Chatbot Demo")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


class ChatRequest(BaseModel):
    message: str = Field(min_length=2, max_length=500)


class ChatResponse(BaseModel):
    answer: str
    confidence: float
    source: str
    matched_question: str | None = None
    next_action: str


@app.get("/")
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    result = find_best_answer(request.message, KNOWLEDGE)

    if result.item:
        return ChatResponse(
            answer=result.item.answer,
            confidence=result.confidence,
            source=result.source,
            matched_question=result.item.question,
            next_action="show_answer",
        )

    if os.getenv("AI_FALLBACK_ENABLED", "false").lower() == "true":
        return ChatResponse(
            answer="I do not have an approved answer yet. In a production project, this is where an AI fallback or human review queue would handle the question.",
            confidence=result.confidence,
            source="ai_fallback_placeholder",
            matched_question=None,
            next_action="route_to_review",
        )

    return ChatResponse(
        answer="I am not fully confident about that answer yet. Please contact support with your order number, or add this question to the knowledge base.",
        confidence=result.confidence,
        source="safe_fallback",
        matched_question=None,
        next_action="route_to_human",
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

