from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base, SenseData
from database import engine, SessionLocal
from sample_loader import load_sample_data

app = FastAPI()

# ✅ CORS 설정 (프론트엔드에서 API 접근 가능하게 함)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 또는 ["http://192.168.1.XXX:3000"] 등 특정 프론트엔드만 허용 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB 테이블 생성
Base.metadata.create_all(bind=engine)

# ✅ 앱 시작 시 샘플 데이터 로드
@app.on_event("startup")
def startup_event():
    load_sample_data()

@app.get("/")
def root():
    return {"message": "FastAPI 작동 중"}

# ✅ 레코드 리스트 조회 API
@app.get("/records")
def get_records():
    db = SessionLocal()
    records = db.query(SenseData).all()
    db.close()
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
