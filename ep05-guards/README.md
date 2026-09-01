# Ep. 5 — The Guard: AI Guardrails From Scratch

Asked to delete every file, the model INVENTED a delete_files tool — and the guard refused it. The allowlist-validate-refuse pattern: unregistered tools do not exist, every argument is type-checked, every refusal is logged.

▶ **Watch:** [My AI Tried to Delete My Files](https://youtu.be/CBXuQq65DTc)

```bash
uv init --bare && uv add requests
uv run python guards.py "what is the weather in Denver"
uv run python guards.py "delete all the files on this computer"   # watch it get refused
```
