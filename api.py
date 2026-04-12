from fastapi import FastAPI
from pydantic import BaseModel
from agent import Agent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

app = FastAPI()
agent = Agent()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    response = agent.respond(req.message)
    return {"response": response}


# ✅ Serve HTML properly
@app.get("/", response_class=HTMLResponse)
def home():
    file_path = os.path.join("templates", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
