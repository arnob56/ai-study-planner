from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from datetime import date

from app.database import engine, Base, get_db
from app import models, scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    subjects = db.query(models.Subject).all()
    return templates.TemplateResponse("index.html", {"request": request, "subjects": subjects})

@app.post("/add")
def add_subject(
    name: str = Form(...),
    difficulty: int = Form(...),
    exam_date: date = Form(...),
    db: Session = Depends(get_db)
):
    subject = models.Subject(name=name, difficulty=difficulty, exam_date=exam_date)
    db.add(subject)
    db.commit()
    return {"message": "Added"}

@app.get("/generate")
def generate(db: Session = Depends(get_db)):
    subjects = db.query(models.Subject).all()
    return scheduler.generate_schedule(subjects)
