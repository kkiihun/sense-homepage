import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# init_db.py
from database import engine
from models import Base

Base.metadata.create_all(bind=engine)
