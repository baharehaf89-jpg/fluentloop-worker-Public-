from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "FluentLoop AI is running"}

@app.post("/chat")
def chat(req: ChatRequest):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": req.message
                }
            ]
        }
    )

    data = response.json()

    return {
        "reply": data["choices"][0]["message"]["content"]
    }
