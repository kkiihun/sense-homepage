from sqlalchemy import Column, Integer, String, Float
from database import Base

class SenseData(Base):
    __tablename__ = "sense_data"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    location = Column(String)
    sense_type = Column(String)
    keyword = Column(String)
    emotion_score = Column(Float)
    description = Column(String)
