from fastapi import APIRouter
import requests

router = APIRouter()

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "phi3"


@router.post("/chat")
def chat(req: dict):
    message = req.get("message", "").strip()
    mode = req.get("mode", "auto")  # auto | offline | online

    if not message:
        return {"response": "⚠️ Please enter a message"}

    # =========================
    # OFFLINE (OLLAMA)
    # =========================
    if mode in ["offline", "auto"]:
        try:
            response = requests.post(
                OLLAMA_URL,
                json={"model": MODEL_NAME, "prompt": message, "stream": False},
                headers={"Content-Type": "application/json"},
                timeout=60,
            )

            if response.status_code == 200:
                data = response.json()

                # safe extraction
                ai_response = data.get("response", "").strip()

                if ai_response:
                    return {"response": ai_response}
                else:
                    print("⚠️ Empty response from Ollama")

            else:
                print(f"⚠️ Ollama HTTP error: {response.status_code}")

        except requests.exceptions.Timeout:
            print("❌ Ollama timeout")

        except Exception as e:
            print("❌ Ollama error:", str(e))

        # if strictly offline mode → stop here
        if mode == "offline":
            return {"response": "⚠️ Offline model failed. Try again."}

    # =========================
    # ONLINE FALLBACK
    # =========================
    try:
        # 🔥 Replace this later with real API (OpenAI/Groq)
        return {"response": f"🌐 (Fallback) You said: {message}"}

    except Exception as e:
        print("❌ Online fallback error:", str(e))
        return {"response": "⚠️ Both offline & online failed"}
