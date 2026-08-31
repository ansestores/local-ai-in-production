from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="gateway")

@app.get("/health")
def health() -> str:
    return "ok"

class ChatIn(BaseModel):
    q: str

@app.post("/v1/chat")
def chat(body: ChatIn) -> dict:
    return {"decision": "tool_call", "input": body.q}
