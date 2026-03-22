<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00C6FF&height=200&section=header&text=AI%20Developer%20Agent&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-FastAPI-blue?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/AI-Ollama-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML/CSS/JS-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Debugger-Agent-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deploy-Render-purple?style=for-the-badge&logo=render" />
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,html,css,js,git,github" />
</p>

---

# 🤖 AI Developer Agent

🌐 Live Demo: https://ai-developer-agent-olive.vercel.app

A **full-stack AI-powered developer tool** that combines chat, debugging, and code execution into one seamless platform.

---

## ✨ Features

### 💬 AI Chat System
- ChatGPT-style interface  
- Clean sidebar navigation  
- Real-time interaction  
- Offline + online fallback  

### 🛠 AI Debugger
- Multi-step debugging loop  
- Error → Fix → Run system  
- Step-by-step debugging history  
- Smart code correction  

### ⚡ Code Execution Engine
- Instant code execution  
- Supports:
  - 🐍 Python  
  - 💻 C (GCC compile + run)  
- Handles runtime & compile errors  

### 🧠 AI Agent Loop

Error → Analyze → Fix → Execute → Repeat

---

### 🎨 UI/UX
- ChatGPT-like interface  
- Dark modern theme  
- Smooth animations  
- Responsive layout  

---

## 🛠 Tech Stack

Backend: FastAPI • Python • Subprocess • Ollama  
Frontend: HTML • CSS • JavaScript  
Deployment: Vercel • Render  

---

## 📂 Project Structure

```bash
ai-dev-agent/
│
├── backend/
│   ├── app.py
│   │
│   ├── agents/
│   │   ├── debugger.py
│   │   ├── executor.py
│   │   └── llm.py
│   │
│   ├── routes/
│   │   ├── chat.py
│   │   └── code.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── chat.html
│   ├── debug.html
│   └── env.js
│
├── Dockerfile
└── .gitignore
```
---

## ⚙️ Local Setup
```
git clone https://github.com/adityasing9/AI-Developer-Agent.git  

cd AI-Developer-Agent  
```
### Backend
```
cd backend  

pip install -r requirements.txt  

uvicorn app:app --reload  
```
### Frontend
```
Open: frontend/index.html  
```
---

## 🌐 Environment Config
```
window.ENV = {  
  API_URL: "https://your-backend-url"  
};
```
---

## ⚠️ Limitations

- Local AI (Ollama) not available in cloud  
- Uses fallback responses in deployment  
- No persistent database  

---

## 🚀 Future Improvements

- 🔐 Authentication system  
- 🧠 Better AI (OpenAI / Groq)  
- 💾 Cloud chat history  
- 🌐 More languages (C++, Java)  
- 📊 Visual debugging UI  

---

# 🚀 System Breakdown

## 🧠 AI Debugging Engine
- Executes code using subprocess  
- Captures errors  
- Sends error to AI  
- Extracts fixed code  
- Re-runs automatically  

---

## ⚡ Execution Engine
- Python via temp files  
- C via GCC compilation  
- Handles syntax, runtime, and compile errors  

---

## 🔁 Agent Loop System
- Multi-step retry logic  
- Stops after 3 attempts  
- Maintains debugging history  
- Prevents infinite loops  

---

## 🌐 API System
- /chat → AI chat  
- /debug → debug loop  
- /run → code execution  

---

## 🎨 Frontend System
- ChatGPT-style layout  
- Sidebar navigation  
- Debug panel  
- API via env.js  

---

## 🚀 Deployment Architecture

Frontend → Vercel  
Backend → Render  
API → Connected via env config  

---

## 👨‍💻 Author

Aditya Singh  
https://github.com/adityasing9  

---

<p align="center">
  ⭐ If you like this project, give it a star!
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,100:00C6FF&height=120&section=footer"/>
</p>