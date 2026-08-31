import json, requests

def embed(text):
    r = requests.post("http://localhost:11434/api/embeddings",
                      json={"model": "nomic-embed-text", "prompt": text})
    return r.json()["embedding"]

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    return dot / ((sum(x*x for x in a)**.5) * (sum(y*y for y in b)**.5))

def answer(question):
    index = json.load(open("index.json"))
    qvec = embed(question)
    top = sorted(index, key=lambda c: cosine(qvec, c["vector"]), reverse=True)[:3]
    context = "\n\n".join(f"[{c['source']}]\n{c['text']}" for c in top)
    prompt = (f"Answer using ONLY the context below. If the answer is not in the "
              f"context, say so.\n\nContext:\n{context}\n\nQuestion: {question}")
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "gemma4:12b", "prompt": prompt, "stream": False})
    return {"answer": r.json()["response"].strip(),
            "sources": list(dict.fromkeys(c["source"] for c in top))}
