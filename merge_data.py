# merge_data.py
import pandas as pd

def load_and_merge():
    """
    Load and merge HR-Employee.csv and UpdatedResumeDataSet.csv.
    """
    hr = pd.read_csv(r"C:/Users/PRUSHOTHAM/Downloads/HR-Employee.csv")
    resumes = pd.read_csv(r"C:/Users/PRUSHOTHAM/Downloads/UpdatedResumeDataSet.csv")


    print("✅ Datasets loaded successfully.")
    print("HR:", hr.shape, "Resumes:", resumes.shape)

    # Basic cleaning
    hr["JobRole"] = hr["JobRole"].astype(str).str.lower()
    resumes["Resume"] = resumes["Resume"].astype(str).str.lower()

    # Compute a simple overlap score between job title and resume text
    def skill_match(jobrole, resume):
        job_words = set(jobrole.split())
        res_words = set(resume.split())
        if not job_words:
            return 0
        return len(job_words & res_words) / len(job_words)

    merged_rows = []
    for _, job in hr.iterrows():
        for _, res in resumes.iterrows():
            merged_rows.append({
                "JobRole": job["JobRole"],
                "Gender": job.get("Gender", "Unknown"),
                "ResumeCategory": res["Category"],
                "SkillMatchScore": skill_match(job["JobRole"], res["Resume"]),
            })

    merged_df = pd.DataFrame(merged_rows)
    print("✅ Combined dataset:", merged_df.shape)
    return merged_df
