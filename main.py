import google.generativeai as genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ---------- CONFIGURE GEMINI ----------
# ⚠️ Replace this with your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------- FASTAPI APP ----------
app = FastAPI()

# Allow frontend (React, Streamlit, etc.) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # In production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- REQUEST MODEL ----------
class CareerRequest(BaseModel):
    query: str

# ---------- ROUTES ----------
@app.get("/")
def home():
    return {"message": "Career Advisor AI Backend is running 🚀"}

@app.post("/ask")
async def ask_career(request: CareerRequest):
    try:
        response = model.generate_content(request.query)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
