import streamlit as st
import pandas as pd
from utils import read_any_file
from sentence_transformers import SentenceTransformer, util

# Load model once
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

st.title("🤖 AI Resume Evaluator for Hiring Systems")
st.markdown("This app compares job descriptions and candidate resumes using **semantic similarity** with AI embeddings.")

# Upload Job Description
st.subheader("📄 Upload Job Description (CSV, PDF, DOCX, or TXT)")
job_file = st.file_uploader("Upload job description file", type=["csv", "pdf", "docx", "txt", "xlsx"])

# Upload Resume Files
st.subheader("👩‍💼 Upload Candidate Resume(s) (CSV, PDF, DOCX, or TXT)")
resume_files = st.file_uploader("Upload one or more resumes", type=["csv", "pdf", "docx", "txt", "xlsx"], accept_multiple_files=True)

# Evaluate button appears only when both job and resumes are uploaded
if job_file and resume_files:
    try:
        job_df = read_any_file(job_file)
        if "text" in job_df.columns:
            job_text = job_df["text"].iloc[0]
        else:
            job_text = " ".join(job_df.astype(str).values.flatten())

        resume_texts = []
        names = []
        for file in resume_files:
            df = read_any_file(file)
            text = df["text"].iloc[0] if "text" in df.columns else " ".join(df.astype(str).values.flatten())
            resume_texts.append(text)
            names.append(file.name)

        st.success(f"✅ Loaded {len(resume_files)} resumes successfully!")

        with st.expander("👀 Preview Extracted Resume Text"):
            for i, text in enumerate(resume_texts):
                st.write(f"**{names[i]}:**")
                st.text(text[:500])

        # Add evaluation button
        if st.button("🔍 Evaluate Candidates"):
            st.info("Analyzing resumes with AI embeddings... Please wait ⏳")

            job_embedding = model.encode(job_text, convert_to_tensor=True)
            resume_embeddings = model.encode(resume_texts, convert_to_tensor=True)
            similarities = util.pytorch_cos_sim(job_embedding, resume_embeddings).tolist()[0]

            results = pd.DataFrame({
                "Candidate": names,
                "Match Score": [round(score * 100, 2) for score in similarities]
            }).sort_values(by="Match Score", ascending=False).reset_index(drop=True)

            st.success("✅ Evaluation complete! Top matching candidates:")
            st.dataframe(results)

            st.bar_chart(results.set_index("Candidate"))

    except Exception as e:
        st.error(f"Error: {e}")
