# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:MyPassWord12@localhost/dbname"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # SQLite일 때만
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
