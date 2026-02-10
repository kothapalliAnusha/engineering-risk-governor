from fastapi import FastAPI
import pickle
import os

from analysis.analyze_diff import analyze_code_change
from policy.decision_engine import policy_decision
from genai.explain_risk import explain_risk

app = FastAPI()

# --- FIXED PATH HANDLING ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "risk_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.post("/analyze-change")
def analyze_change(lines_changed: int, functions_changed: int, complexity: int):
    features = analyze_code_change(lines_changed, functions_changed, complexity)

    risk_score = model.predict_proba([[
        features["lines_changed"],
        features["functions_changed"],
        features["complexity"]
    ]])[0][1]

    decision = policy_decision(risk_score)
    explanation = explain_risk(features, risk_score)

    return {
        "risk_score": round(float(risk_score), 2),
        "decision": decision,
        "explanation": explanation
    }
