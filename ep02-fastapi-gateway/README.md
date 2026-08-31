# Ep. 2 — The Gateway Skeleton (16 lines)

The entire server from Episode 2: a FastAPI app with a health check and a typed chat route.

▶ **Watch:** [FastAPI + Local LLM Tutorial: Build an AI Gateway in 16 Lines](https://youtu.be/QYCVhOCUPDk)

```bash
uv init --bare && uv add fastapi uvicorn
uv run uvicorn app:app --port 8091
curl localhost:8091/health
```
