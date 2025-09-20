🚀 AI Career Strategist

- AI Career Strategist is an intelligent web application that helps users bridge the gap between their current skills and their career goals.
- It analyzes resumes or manually entered skills, compares them with desired job roles or skill sets, and generates a personalized strategic learning plan with timelines, projects, and course recommendations.

✨ Features

📄 Resume Analyzer
- Upload your PDF/DOCX resume.
- Auto-extracts text and identifies missing/essential skills.

📝 Manual Skill Entry
- Enter your skills and projects manually if you don’t want to upload a resume.

🎯 Goal-Oriented Planning
- Paste a job description or describe your dream skillset.
- Define your target proficiency level (Proficient, Job-Ready, Expert).

⏳ Timeline Customization
- Choose duration (3 months, 6 months, 1 year) and study hours per month.

📊 Interactive Results Dashboard
- Job Match Score visualization.
- Priority skills list.
- High-level learning timeline (Chart.js).
- Step-by-step roadmap with tasks.
- Suggested hands-on projects and online courses.

🤖 AI Tutor & Chatbot
- Integrated AI assistant to explain concepts in analogies, technical definitions, and prerequisites.
- Floating chatbot for asking questions about your career plan.

📥 Export Plan as PDF
- Download your personalized roadmap in a neat, shareable PDF format.

🛠️ Tech Stack

-Frontend
   - HTML5, CSS3 (custom design system)
   - JavaScript (ES Modules)
   - Chart.js (visualizations)
   - Mammoth.js (DOCX text extraction)
   - PDF.js (PDF text extraction)
   - HTML2PDF.js (plan export)

-Backend
   - Python (FastAPI)
   - Pydantic (data validation)
   - CORS Middleware (frontend-backend communication)

📂 Project Structure

career-advisor-ai/
│── backend/
│   └── main.py          # FastAPI backend (resume analyzer)
│
│── frontend/
│   ├── index.html       # Main UI
│   ├── style.css        # Styling
│   ├── script.js        # Frontend logic
│   ├── download-icon.svg
│
│── README.md            # Documentation


⚡ Installation & Setup

1️⃣ Clone the Repository
- git clone https://github.com/Vanduputti/career-advisor-ai.git
  -cd career-advisor-ai

2️⃣ Backend Setup (FastAPI)
-Make sure you have Python 3.9+ installed.
   -cd backend
   -pip install fastapi uvicorn pydantic 
-Run the FastAPI server:
   -uvicorn main:app --reload

✅ Backend will start at: http://127.0.0.1:8000/
3️⃣ Frontend Setup

Simply open frontend/index.html in your browser.
(Or use Live Server in VS Code for smoother dev experience.)

🎯 Usage

1. Open the app in your browser.
2. Upload a resume or enter skills manually.
3. Paste job description / career goal.
4. Choose your timeline and hours.
5. Click Generate My Strategic Plan.
6. Explore:
   - Job Match Score
   - Skills to Learn
   - Roadmap & Projects
   - AI Chatbot for explanations
7. Download your personalized plan as PDF.

🔮 Future Enhancements
- ✅ AI-powered resume scoring with GPT models.
- ✅ Personalized course links from Coursera/edX/YouTube.
- ✅ Save and track progress over time.
- ✅ Multi-language support for wider accessibility.

👩‍💻 Author
-Vandana D L and Team
- Building AI-driven solutions for career growth and financial inclusion.


