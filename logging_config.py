# logging_config.py
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# 로그 디렉토리 생성
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 핸들러 설정: 매일 자정마다 로그 분리 (backupCount=7은 최근 7일 유지)
handler = TimedRotatingFileHandler(
    filename=os.path.join(LOG_DIR, "sense_backend.log"),
    when="midnight",    # 매일 자정마다 롤오버
    interval=1,
    backupCount=10,     # 10일간 로그 파일 유지
    encoding="utf-8"
)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 루트 로거 설정
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)
