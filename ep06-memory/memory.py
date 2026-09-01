import json, os, sys, requests

STORE = "memory.json"

def load():
    return json.load(open(STORE)) if os.path.exists(STORE) else []

def save(turns):
    json.dump(turns[-20:], open(STORE, "w"), indent=1)   # keep the last 20 turns

def ask(question):
    turns = load()
    history = "\n".join(f"{t['role']}: {t['text']}" for t in turns)
    prompt = (f"Continue this conversation. Use the history to resolve references "
              f"like 'it' or 'that'.\n\n{history}\nuser: {question}\nassistant:")
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "gemma4:12b", "prompt": prompt, "stream": False})
    answer = r.json()["response"].strip()
    turns += [{"role": "user", "text": question}, {"role": "assistant", "text": answer}]
    save(turns)
    print(answer)

ask(" ".join(sys.argv[1:]))
