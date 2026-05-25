import requests

def ask_ai(prompt):

    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )

    data = response.json()

    return data["response"]


answer = ask_ai("Explain Python loops")

print(answer)