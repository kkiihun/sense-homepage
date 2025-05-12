from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 환경에 따라 다르게 설정
DATABASE_URL = "postgresql://postgres:MyPassWord12@localhost:5432/sense_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # ✅ 이 줄이 꼭 있어야 함
