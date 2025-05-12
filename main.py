from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import Base, SenseData
from database import engine, SessionLocal
from sample_loader import load_sample_data
from logging_config import logger 

app = FastAPI()

# ✅ CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 필요시 프론트엔드 주소로 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB 테이블 생성
Base.metadata.create_all(bind=engine)

# ✅ 샘플 데이터 로드
@app.on_event("startup")
def startup_event():
    logger.info("서버 시작됨")
    try:
        load_sample_data()
        logger.info("샘플 데이터 로드 완료")
    except Exception as e:
        logger.error(f"샘플 데이터 로드 중 오류 발생: {e}")
    
@app.get("/")
def root():
    return {"message": "FastAPI 작동 중"}

# ✅ 레코드 조회
@app.get("/records")
def get_records():
    db = SessionLocal()
    try:
        records = db.query(SenseData).all()     
        return [
        {
            "id": r.id,
            "date": r.date,
            "location": r.location,
            "sense_type": r.sense_type,
            "keyword": r.keyword,
            "emotion_score": r.emotion_score,
            "description": r.description
        }
        for r in records
    ]
    finally:
        db.close()

# ✅ 업로드용 Pydantic 모델
class SenseInput(BaseModel):
    date: str
    location: str
    sense_type: str
    keyword: str
    emotion_score: int
    description: str

# ✅ 업로드 API
@app.post("/upload")
def upload_record(data: SenseInput):
    db = SessionLocal()
    try:
        record = SenseData(**data.dict())
        db.add(record)
        db.commit()
        db.refresh(record)
        return {"message": "업로드 성공", "id": record.id}    
    finally:
        db.close()
    

