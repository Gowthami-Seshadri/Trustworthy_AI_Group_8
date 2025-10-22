import pandas as pd
import pdfplumber
import docx

def read_any_file(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    elif file_name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8", errors="ignore")
        return pd.DataFrame({"text": [text]})

    elif file_name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return pd.DataFrame({"text": [text]})

    elif file_name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n".join([p.text for p in doc.paragraphs])
        return pd.DataFrame({"text": [text]})

    else:
        raise ValueError("Unsupported file type! Please upload CSV, PDF, DOCX, or TXT.")
