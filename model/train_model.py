import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("../data/risk_data.csv")

X = df[["lines_changed", "functions_changed", "complexity"]]
y = df["risk"]

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

with open("risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Risk model trained and saved.")
