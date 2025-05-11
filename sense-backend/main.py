from fastapi import FastAPI
from routes import data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # ← 이 부분 꼭 필요

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ 프론트 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
