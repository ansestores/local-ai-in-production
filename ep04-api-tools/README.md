# Ep. 4 — Turn Any API Into an AI Tool

The "cloud decides, app executes" pattern in ~35 lines: the local model picks a tool and its arguments as JSON, YOUR code executes the real API call, and the model summarizes the result. Uses open-meteo (free, no key).

▶ **Watch:** [Give Your Local AI Tools — Function Calling From Scratch](https://youtu.be/GVjoBXm0uio)

```bash
uv init --bare && uv add requests
uv run python tools.py "what is the weather in Miami right now"
```

Add your own tools to the TOOLS dict — every function you register becomes something the assistant can DO.
