# src/api.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib
from merge_data import load_and_merge

app = Flask(__name__)

model = joblib.load("../models/rf_model.pkl")
df = load_and_merge()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    skill_match = data["skill_match_score"]
    exp_gap = data["experience_gap"]
    age = data["age"]

    pred = model.predict([[skill_match, exp_gap, age]])[0]
    prob = model.predict_proba([[skill_match, exp_gap, age]])[0][1]

    return jsonify({"match_prediction": int(pred), "probability": round(float(prob), 2)})

@app.route("/suggest_top", methods=["GET"])
def suggest_top():
    df["pred_prob"] = model.predict_proba(df[["skill_match_score", "experience_gap", "age"]])[:, 1]
    top_candidates = df.sort_values("pred_prob", ascending=False).head(5)
    results = top_candidates[["job_title", "name", "pred_prob", "gender", "age"]].to_dict(orient="records")
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
