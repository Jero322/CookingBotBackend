from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os  # Needed for environment variables

app = FastAPI()


GOOGLE_API_KEY = "AIzaSyArBpUgIFeeDE-HFqxu-O-7QLwyw5vyI2k"  # 🔴 Replace with your real key

# Option 2: Better - use environment variable
# GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")  # Set this in your system first

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")
# ============================== #

class ChatRequest(BaseModel):
    mensaje: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = model.generate_content(request.mensaje)
        return {"respuesta": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "Use POST /chat with {'mensaje':'your message'}"}