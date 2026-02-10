# Engineering Risk Governor (GenAI + ML)
### Failure Prediction & Prevention Prototype

Engineering Risk Governor is a prototype system that predicts **risky software changes before deployment**.  
It analyzes code change characteristics, estimates failure risk using machine learning, and provides **clear, explainable insights** to support safer merge decisions.

---

## Problem
Software failures are often detected **after deployment**, leading to outages and rework.  
Manual code reviews are subjective and may miss hidden risk patterns.

---

## Solution
This system evaluates code changes **before merge** and:
- Predicts failure risk using ML
- Explains risk in human-readable terms
- Applies policy-based decisions (Approve / Review / Block)

---

## Key Features
- ML-based risk prediction (Random Forest)
- Explainable decision logic (GenAI-style explanations)
- Policy-based governance
- FastAPI-powered REST endpoint
- Fully local, reproducible prototype

---

## Tech Stack
Python, scikit-learn, FastAPI, Git

---

## How to Run
```bash
pip install -r requirements.txt
cd model
python train_model.py
cd ..
uvicorn api.main:app --reload

```
Test at:

http://127.0.0.1:8000/docs

Sample Output
{
  "risk_score": 0.94,
  "decision": "BLOCK",
  "explanation": "The code change modifies 200 lines and 5 functions, indicating high failure risk."
}

Note

This is a working prototype using simulated data, built to demonstrate system design, ML integration, and explainability.

## Author
K. Anusha


