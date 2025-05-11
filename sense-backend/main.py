# main.py
from fastapi import FastAPI
from models import Base
from database import engine
from sample_loader import load_sample_data

app = FastAPI()

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    load_sample_data()

@app.get("/")
def root():
    return {"message": "FastAPI 작동 중"}
