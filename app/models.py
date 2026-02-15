from sqlalchemy import Column, Integer, String, Date, Float
from app.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    difficulty = Column(Integer)
    exam_date = Column(Date)

class Performance(Base):
    __tablename__ = "performance"

    id = Column(Integer, primary_key=True)
    difficulty = Column(Integer)
    days_left = Column(Integer)
    focus_score = Column(Float)
    completion_rate = Column(Float)
    actual_hours = Column(Float)
