# 🚀 Career Advisor AI

**Career Advisor AI** is an AI-powered Personalized Career & Skills Advisor that recommends career paths, performs skill gap analysis, and generates learning paths.  
Built with **FastAPI (backend)** and **Streamlit (frontend)** and optionally powered by the Gemini / Google Generative AI.

---

## 📂 Project Structure

career-advisor-ai/
├── backend/ # FastAPI backend (APIs)
│ ├── main.py
│ └── test.py
├── frontend/ # Streamlit frontend (UI)
│ └── app.py
├── data/ # Sample datasets for testing
│ ├── careers.csv
│ └── careers.json
├── requirements.txt
└── README.md


---

## ⚡ Features

- AI-based career recommendations (via Gemini / LLM)
- Skill gap analysis & recommended learning path
- FastAPI backend with JSON endpoints
- Streamlit frontend for interactive demo
- Easy local setup and cloud deployment

---

## 🔧 Quick Setup

> Make sure you are in the project root `career-advisor-ai/`

### 1. Create and activate virtual environment
**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

macOS / Linux
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

If you run into dependency conflicts, create a fresh virtual environment and install minimal required packages:
pip install fastapi uvicorn streamlit google-generativeai requests pandas python-dotenv

▶️ Run Locally
1) Start the backend (FastAPI)
cd backend
uvicorn main:app --reload


Backend default: http://127.0.0.1:8000
Swagger UI: http://127.0.0.1:8000/docs

Example health check:
GET http://127.0.0.1:8000/

2) Start the frontend (Streamlit)

Open a new terminal (keep backend running):

cd frontend
streamlit run app.py

Streamlit UI: http://localhost:8501
🌐 Example API Usage
POST /ask (example)

Request
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"query": "Suggest top AI careers for a student who knows Python and ML"}'


Expected Response (JSON)

{
  "response": "1. Data Scientist — ...\n2. ML Engineer — ...\n3. Prompt Engineer — ..."
}

📁 Sample data (in data/)

data/careers.csv (example rows)

Career,Skills,Average_Salary,Domain
Data Scientist,Python; Machine Learning; Statistics,120000,Data Science
Software Engineer,Java; C++; Problem Solving,100000,Software Development
AI Researcher,Deep Learning; NLP; Research,130000,Artificial Intelligence
UI/UX Designer,Wireframing; Figma; Creativity,80000,Design
Cybersecurity Analyst,Networking; Security; Risk Analysis,95000,Cybersecurity

data/careers.json (example)

[
  {
    "career": "Data Scientist",
    "skills": ["Python", "Machine Learning", "Statistics"],
    "average_salary": 120000,
    "domain": "Data Science"
  }
]


Your backend can load these files and match user skills to roles.

🧭 How it works (high level)
Frontend (Streamlit) sends user input (skills / question) to backend /ask.
Backend (FastAPI) either:
Performs local matching using data/careers.csv (skill overlap / embeddings), or
Calls Gemini/LLM (google-generativeai) to generate personalized learning path + interview tips.
Backend returns structured plain text or JSON; frontend renders it.

🔐 Environment & API Keys
Keep your LLM/API keys out of source control.
Use a .env file + python-dotenv or platform secrets manager.
Example .env (do not commit):
GEMINI_API_KEY=your_api_key_here


Load in Python (example):
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

🚀 Deployment (quick notes)
Frontend: Streamlit Cloud (share.streamlit.io) — easiest for quick demos.
Backend: Render, Railway, or Heroku — host FastAPI and provide a public URL.
After deploying backend, update frontend/app.py backend URL to the public one.
Render start command example:
uvicorn main:app --host 0.0.0.0 --port 10000

🧪 Troubleshooting Tips
Error: File does not exist: app.py → ensure you run streamlit run app.py from the frontend/ folder where app.py exists.
PermissionDenied or 403 with Gemini → enable Generative Language API for the correct Google Cloud project and ensure billing/credentials are correct.
Dependency conflicts → use a fresh venv and install minimal required packages; pin versions in requirements.txt after confirming.

✅ Useful Commands (summary)
# from project root
# create venv (Windows)
python -m venv venv
.\venv\Scripts\Activate.ps1

# install
pip install -r requirements.txt

# run backend
cd backend
uvicorn main:app --reload

# run frontend (in new terminal)
cd frontend
streamlit run app.py

🧾 Author
Vandana D L (Vandanaputti)
Email: vandanadlputti@gmail.com

If you want, I can:
Add example screenshots to the README,
Add ready-made badge links (build/deploy),
Or generate a Contributing and License section.
