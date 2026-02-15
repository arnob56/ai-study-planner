from app.ml_engine import predict_hours

def generate_schedule(subjects):
    schedule = []

    for sub in subjects:
        hours = predict_hours(sub)
        schedule.append({
            "subject": sub.name,
            "hours": round(hours, 2)
        })

    return schedule
