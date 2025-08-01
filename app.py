import streamlit as st
from utils.resume_parser import extract_text_from_file
from utils.scorer import calculate_score, find_missing_keywords

st.set_page_config(page_title="ATS Resume Score Analyzer", layout="centered")

st.title("📄 ATS Resume Score Analyzer")
st.write("Upload your resume and paste a job description to get an ATS compatibility score.")

resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description here", height=200)

if st.button("Analyze"):
    if resume_file and jd_text.strip():
        resume_text = extract_text_from_file(resume_file)
        score = calculate_score(resume_text, jd_text)
        missing = find_missing_keywords(resume_text, jd_text)

        st.success(f"✅ ATS Match Score: {score} / 100")
        if missing:
            st.warning("Missing keywords in resume:")
            st.write(", ".join(missing))
        else:
            st.info("All important keywords from the job description are present in your resume!")
    else:
        st.error("Please upload a resume and paste a job description.")
