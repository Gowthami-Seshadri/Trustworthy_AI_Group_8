# merge_data.py
import pandas as pd

def load_and_merge():
    """
    Load HR-Employee.csv and UpdatedResumeDataSet.csv,
    clean text, and combine into a single DataFrame with skill match scores.
    """
    
    hr = pd.read_csv(r"C:/Users/PRUSHOTHAM/Downloads/HR-Employee.csv")
    resumes = pd.read_csv(r"C:/Users/PRUSHOTHAM/Downloads/UpdatedResumeDataSet.csv")

    print("✅ Datasets loaded:")
    print("HR shape:", hr.shape, "Resumes shape:", resumes.shape)

    # Clean text
    resumes["Resume"] = resumes["Resume"].astype(str).str.lower()
    hr["JobRole"] = hr["JobRole"].astype(str).str.lower()

    # Compute simple text overlap for now
    def skill_match(jobrole, resume):
        job_words = set(str(jobrole).split())
        res_words = set(str(resume).split())
        return len(job_words & res_words) / (len(job_words) + 1e-5)

    merged_data = []
    for _, job in hr.iterrows():
        for _, res in resumes.iterrows():
            merged_data.append({
                "JobRole": job["JobRole"],
                "Gender": job.get("Gender", "Unknown"),
                "ResumeCategory": res["Category"],
                "ResumeText": res["Resume"][:200],
                "SkillMatchScore": skill_match(job["JobRole"], res["Resume"])
            })

    df = pd.DataFrame(merged_data)
    print("✅ Combined dataset:", df.shape)
    return df
