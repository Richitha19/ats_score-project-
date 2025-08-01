# ATS Resume Score Analyzer

A web-based tool built with Streamlit to evaluate how well a resume matches a given job description using basic NLP techniques. Designed to simulate how Applicant Tracking Systems (ATS) filter resumes before they reach a recruiter.

## 🔍 Features

- 📄 Upload and analyze PDF or DOCX resumes.
- 📑 Input a Job Description manually.
- 🧠 Extracts and compares key skills from resume and JD.
- 📊 Generates a matching **score out of 100**.
- 📈 Visual indicators for resume-JD match quality.
- ⚡ Simple, fast, and beginner-friendly UI using Streamlit.

## 🛠️ Tech Stack

- Python 3
- Streamlit
- PyPDF2
- python-docx
- Scikit-learn

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ATS_Resume_Score_Analyzer.git
   cd ATS_Resume_Score_Analyzer


Install dependencies:  pip install -r requirements.txt

Run the app:  streamlit run app.py
Open in browser:
It will auto-launch or go to: http://localhost:8501



ATS_Resume_Score_Analyzer/
├── app.py
├── utils/
│   ├── jd_parser.py
│   └── resume_parser.py
├── sample_data/
│   ├── sample_resume.pdf
│   └── sample_jd.txt
├── requirements.txt
└── README.md

This project is for educational and demo purposes.
