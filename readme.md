# SENSE 데이터마켓 플랫폼

AI와 감성 데이터를 연결하는 데이터 커머스 플랫폼입니다. 
사용자는 감각(향, 맛, 시각 등)에 대한 주관적인 데이터를 입력하고,
이를 차트로 시각화하고, 데이터 마켓 형태로 확장할 수 있습니다.

---

## 주요 기술 스택

### Frontend (`/sense-frontend`)
- **Next.js** (v15)
- **TypeScript**
- **Tailwind CSS**
- **Chart.js** + `react-chartjs-2`
- **REST API 연동** (`fetch`)

### Backend (`/sense-backend`)
- **FastAPI**
- **Python 3.13**
- **SQLAlchemy**
- **PostgreSQL** (v15)
- **Uvicorn**, **dotenv**

---

## 기능 요약

| 기능 | 설명 |
|------|------|
| 감각 데이터 입력 | `/upload` API로 사용자 감각 데이터 등록 (향, 맛 등) |
| 데이터 조회 | `/records` API로 전체 감각 데이터 불러오기 |
| 데이터 시각화 | 감각 유형별 평균 감정점수 Pie/Bar Chart 시각화 |
| UI 디자인 | KDX 느낌의 데이터 커머스 형태로 구성 |

---

## 프로젝트 구조

```
sense_homepage/
├── sense-frontend/       # 프론트엔드 (Next.js)
│   ├── pages/
│   │   └── index.tsx
│   ├── components/
│   │   ├── EmotionChart.tsx
│   │   └── UploadForm.tsx (예정)
│   └── styles/globals.css
│
├── sense-backend/        # 백엔드 (FastAPI)
│   ├── main.py
│   ├── routes/data.py
│   ├── models.py
│   ├── database.py
│   └── init_db.py
```

---

## 설치 및 실행 방법

### 1. 백엔드 실행 (FastAPI)
```bash
cd sense-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. 프론트엔드 실행 (Next.js)
```bash
cd sense-frontend
npm install
npm run dev
```

접속: [http://localhost:3000](http://localhost:3000)

---

## API 명세

### `POST /upload`
- 감각 데이터를 업로드합니다.
- 필드: `date`, `location`, `sense_type`, `keyword`, `emotion_score`, `description`

### `GET /records`
- 전체 감각 데이터를 JSON 형식으로 반환합니다.

---

## 향후 확장 계획
- [ ] 감각 데이터 입력폼 UploadForm 컴포넌트 추가
- [ ] CSV 다운로드 기능 추가
- [ ] 지역/날짜별 감정 트렌드 대시보드
- [ ] 데이터 판매용 마켓 페이지 구축 (KDX 스타일)

---

## 라이선스
MIT License
