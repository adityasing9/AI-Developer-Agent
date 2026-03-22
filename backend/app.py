from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from routes import chat, code


# =========================
# APP INIT
# =========================
app = FastAPI(
    title="AI Developer Agent",
    description="Hybrid AI Agent (Ollama + API)",
    version="1.0.0",
)


# =========================
# CORS (Frontend Access)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# ROUTES
# =========================
app.include_router(chat.router, prefix="")
app.include_router(code.router, prefix="")


# =========================
# ROOT ENDPOINT
# =========================
@app.get("/")
def home():
    return {"message": "AI Developer Agent Running 🚀", "status": "ok"}


# =========================
# HEALTH CHECK (important for deployment)
# =========================
@app.get("/health")
def health():
    return {"status": "healthy"}
