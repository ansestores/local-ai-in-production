import json, sys, requests

def get_weather(city):
    geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                       params={"name": city, "count": 1}).json()["results"][0]
    wx = requests.get("https://api.open-meteo.com/v1/forecast",
                      params={"latitude": geo["latitude"], "longitude": geo["longitude"],
                              "current": "temperature_2m,wind_speed_10m"}).json()["current"]
    return f"{geo['name']}: {wx['temperature_2m']}°C, wind {wx['wind_speed_10m']} km/h"

TOOLS = {"get_weather": {"fn": get_weather, "desc": "current weather. args: {city}"}}

def ask(question):
    menu = "\n".join(f"- {n}: {t['desc']}" for n, t in TOOLS.items())
    prompt = (f"You can call ONE tool. Reply with ONLY JSON: "
              f'{{"tool": name, "args": {{...}}}}\nTools:\n{menu}\nQuestion: {question}')
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": "gemma4:12b", "prompt": prompt,
                            "format": "json", "stream": False})
    call = json.loads(r.json()["response"])
    print(f"model chose: {call}")
    result = TOOLS[call["tool"]]["fn"](**call["args"])
    r2 = requests.post("http://localhost:11434/api/generate",
                       json={"model": "gemma4:12b", "stream": False,
                             "prompt": f"Tool returned: {result}\nAnswer briefly: {question}"})
    print(r2.json()["response"].strip())

ask(" ".join(sys.argv[1:]))
