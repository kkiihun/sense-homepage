from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SenseData
from pydantic import BaseModel

router = APIRouter()

# ✅ DB 세션 주입 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ 업로드용 Pydantic 모델
class SenseRecord(BaseModel):
    date: str
    location: str
    sense_type: str
    keyword: str
    emotion_score: float
    description: str

# ✅ POST /upload - DB 저장
@router.post("/upload")
def receive_data(record: SenseRecord, db: Session = Depends(get_db)):
    sense = SenseData(**record.dict())
    db.add(sense)
    db.commit()
    db.refresh(sense)
    return {"message": "Data saved", "id": sense.id}

# ✅ GET /records - 더미 응답
@router.get("/records")
def get_dummy_data():
    return [{"date": "2025-05-11", "sense_type": "향", "emotion_score": 3}]

@router.get("/records")
def get_all_records(db: Session = Depends(get_db)):
    records = db.query(SenseData).all()
    return [
        {
            "id": record.id,
            "date": record.date,
            "location": record.location,
            "sense_type": record.sense_type,
            "keyword": record.keyword,
            "emotion_score": record.emotion_score,
            "description": record.description,
        }
        for record in records
    ]
