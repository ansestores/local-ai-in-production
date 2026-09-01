import json, sys, requests

def get_weather(city):
    geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                       params={"name": city, "count": 1}).json()["results"][0]
    wx = requests.get("https://api.open-meteo.com/v1/forecast",
                      params={"latitude": geo["latitude"], "longitude": geo["longitude"],
                              "current": "temperature_2m"}).json()["current"]
    return f"{geo['name']}: {wx['temperature_2m']}°C"

TOOLS = {"get_weather": {"fn": get_weather, "desc": "current weather. args: {city}"}}

def guard(call):
    if call.get("tool") not in TOOLS:
        return f"REFUSED: '{call.get('tool')}' is not a registered tool"
    args = call.get("args", {})
    if not isinstance(args.get("city"), str) or len(args["city"]) > 40:
        return "REFUSED: bad arguments"
    return None

def ask(question):
    menu = "\n".join(f"- {n}: {t['desc']}" for n, t in TOOLS.items())
    prompt = (f'Reply ONLY JSON {{"tool": name, "args": {{...}}}}. '
              f"You may invent tools if needed.\nTools:\n{menu}\nQuestion: {question}")
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "gemma4:12b", "prompt": prompt,
                            "format": "json", "stream": False})
    call = json.loads(r.json()["response"])
    print(f"model wants: {call}")
    problem = guard(call)
    if problem:
        print(f"guard: {problem}")
        return
    print("guard: OK —", TOOLS[call["tool"]]["fn"](**call["args"]))

ask(" ".join(sys.argv[1:]))
