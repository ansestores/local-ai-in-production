import json, pathlib, requests

def embed(text):
    r = requests.post("http://localhost:11434/api/embeddings",
                      json={"model": "nomic-embed-text", "prompt": text})
    return r.json()["embedding"]

index = []
for doc in sorted(pathlib.Path("docs").glob("*.txt")):
    for chunk in doc.read_text().split("\n\n"):
        chunk = chunk.strip()
        if len(chunk) < 40:
            continue
        index.append({"source": doc.name, "text": chunk, "vector": embed(chunk)})
        print(f"embedded {doc.name}: {chunk[:50]}...")

json.dump(index, open("index.json", "w"))
print(f"\nindex.json written - {len(index)} chunks ready to search")
