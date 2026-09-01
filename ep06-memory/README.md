# Ep. 6 — Memory: An Assistant That Remembers

~20 lines. Every turn is appended to `memory.json` and replayed as history on the next call, so the model can resolve "it", "that", and your name. The last-20-turns window keeps the prompt small — the same trick production chat systems use before they reach for a database.

▶ **Watch:** [Give Your Local AI a Memory](https://youtu.be/Xf9l_cF2FXM)

```bash
uv init --bare && uv add requests
uv run python memory.py "My name is Alex and I work on solar panels."
uv run python memory.py "What is my name and what do I work on?"
```
