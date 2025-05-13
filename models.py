# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RecordModel(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False)
    location = Column(String, nullable=False)
    sense_type = Column(String, nullable=False)
    keyword = Column(String, nullable=False)
    emotion_score = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
