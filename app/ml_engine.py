import joblib
import numpy as np
from datetime import date

model = joblib.load("app/model.pkl")

def predict_hours(subject):
    days_left = (subject.exam_date - date.today()).days

    features = np.array([[ 
        subject.difficulty,
        days_left,
        7,
        0.8
    ]])

    return float(model.predict(features)[0])
