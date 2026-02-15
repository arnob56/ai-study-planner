import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from app.database import SessionLocal
from app.models import Performance

db = SessionLocal()
data = db.query(Performance).all()

if not data:
    print("No data to train.")
    exit()

rows = []
for row in data:
    rows.append([
        row.difficulty,
        row.days_left,
        row.focus_score,
        row.completion_rate,
        row.actual_hours
    ])

df = pd.DataFrame(rows, columns=[
    "difficulty", "days_left",
    "focus_score", "completion_rate",
    "actual_hours"
])

X = df[["difficulty", "days_left", "focus_score", "completion_rate"]]
y = df["actual_hours"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "app/model.pkl")

print("Model trained.")
