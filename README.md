Fair AI Resume Evaluator (Trustworthy Hiring System)

Overview:

This project builds an AI-powered resume evaluator that helps organizations automatically match candidate resumes with job descriptions using semantic similarity.
The system uses Sentence-BERT (all-MiniLM-L6-v2) to understand meaning in text and rank candidates based on relevance.
The project also lays the foundation for Trustworthy AI in Hiring, ensuring that candidate evaluations are fair, transparent, and explainable.

How to Run (macOS & Windows):

Step 1:  Clone the Repository

git clone https://github.com/Gowthami-Seshadri/Trustworthy_AI_Group_8.git
cd Trustworthy_AI_Group_8/src

Step 2: Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows


Step 3: Install Dependencies
pip install -r requirements.txt

Step 4 : Execute the Training Model
Python train_model.py 

Step 5: Run the Application
Python -m streamlit run app.py

Once launched, you can:
  1️ Upload a Job Description File.
  2️ Upload one or more Resumes(upto 200mb) (PDF/DOCX/TXT)
  3 Click Evaluate Candidates to view similarity scores and rankings.

  
References and Source Declaration 

External Code Sources:

1.https://github.com/UKPLab/sentence-transformers
2.https://github.com/Trusted-AI/AIF360
3. Gemini AI and Chatgpt
