from fastapi import FastAPI
from pydantic import BaseModel
import rag

app = FastAPI(title="local-ai-platform")

@app.get("/health")
def health() -> str:
    return "ok"

class AskIn(BaseModel):
    q: str

@app.post("/v1/ask")
def ask(body: AskIn) -> dict:
    return rag.answer(body.q)
