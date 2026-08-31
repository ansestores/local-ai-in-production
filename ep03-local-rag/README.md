# Ep. 3 — Local RAG in 42 Lines

Chat with your own documents, 100% offline: `ingest.py` (18 lines) embeds every paragraph with Ollama's `nomic-embed-text`; `ask.py` (24 lines) cosine-searches the top 3 chunks and answers with a grounding rule that refuses to guess.

▶ **Watch:** [Local RAG Tutorial: Chat With Your Own Documents 100% Offline](https://youtu.be/T98q400jJ5s)

```bash
ollama pull nomic-embed-text && ollama pull gemma4:12b
uv init --bare && uv add requests
uv run python ingest.py
uv run python ask.py "how many paid leave days do I get"
```

Drop YOUR `.txt` files in `docs/` and re-run ingest — that's the whole point.
