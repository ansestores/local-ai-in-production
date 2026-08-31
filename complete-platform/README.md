# The Complete Platform — $0, Fully Private

Everything from Episodes 1-3 wired together: a FastAPI server with a `/v1/ask` endpoint that answers questions from YOUR documents using only local models.

▶ **Watch the full build:** (video link coming — magnet build)

```bash
ollama pull gemma4:12b && ollama pull nomic-embed-text
uv init --bare && uv add requests fastapi uvicorn
uv run python ingest.py
uv run uvicorn app:app --port 8091
curl -X POST localhost:8091/v1/ask -H "Content-Type: application/json" \
  -d '{"q":"how many paid leave days do I get"}'
```
