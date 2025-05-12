import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SenseData

sense_types = ["향", "맛", "소리", "시각", "촉감", "온도"]
keywords_by_type = {
    "향": ["라벤더", "커피향", "숲냄새", "바다향기"],
    "맛": ["초콜릿", "녹차", "막걸리", "귤"],
    "소리": ["비", "새소리", "바람", "잔잔한 음악"],
    "시각": ["노을", "달빛", "숲속", "해변"],
    "촉감": ["부드러움", "차가움", "따뜻함", "거침"],
    "온도": ["따뜻한 날", "시원한 날", "쌀쌀한 날", "무더위"]
}
locations = ["서울", "양평", "강릉", "전주", "부산"]
descriptions = [
    "감미롭고 편안한 분위기", "신선하고 상쾌함", "감정을 자극함", "고요하고 평화로움", "복합적인 감각 자극"
]

def load_sample_data():
    db: Session = SessionLocal()

    # 기존 데이터 모두 삭제 (선택사항)
    db.query(SenseData).delete()

    for _ in range(50):
        sense = random.choice(sense_types)
        keyword = random.choice(keywords_by_type[sense])
        record = SenseData(
            date=(datetime.now() - timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d %H:%M:%S"),
            location=random.choice(locations),
            sense_type=sense,
            keyword=keyword,
            emotion_score=round(random.uniform(-5, 5), 1),
            description=random.choice(descriptions)
        )
        db.add(record)
    db.commit()
    db.close()
    print("✅ 다양화된 샘플 데이터 50개 삽입 완료!")
