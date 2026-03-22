import requests

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"


def call_ollama(prompt):
    response = requests.post(
        OLLAMA_URL, json={"model": "qwen2.5:1.5b", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]


def call_api(prompt):
    # Dummy (replace later with OpenAI)
    return "API fallback: " + prompt


def generate_response(prompt, mode="auto"):
    if mode == "offline":
        return call_ollama(prompt)

    elif mode == "online":
        return call_api(prompt)

    else:  # auto
        try:
            return call_ollama(prompt)
        except:
            return call_api(prompt)
