# 🔌 Sense Journey - API 명세서 (API Specification)

> 감각 기록 플랫폼의 핵심 API 정의서  
> 요청 방식, 엔드포인트, 요청/응답 예시, 필드 설명 포함

---

## ✅ 1. 공통 사항

- Base URL: `http://localhost:8000` 또는 추후 서버 도메인
- Content-Type: `application/json`
- 인증 방식: JWT 토큰 기반 (추후 구현 예정)

---

## 📝 2. 감각 기록 관련 API

### 📌 2.1. 감각 기록 등록 (Create Record)

- **Endpoint:** `POST /records`
- **Description:** 감각 체험 기록 저장
- **Request Body:**
```json
{
  "date": "2025-05-14",
  "location": "광화문",
  "sense_type": "청각",
  "keyword": "종소리, 고요함",
  "emotion_score": 3,
  "description": "조용한 거리에서 은은한 종소리를 들음",
  "image_url": "http://example.com/image.jpg",
  "audio_url": "http://example.com/audio.mp3"
}
```

- **Response:**
```json
{
  "message": "Record saved successfully",
  "id": 17
}
```
### 📌 2.2. 감각 기록 전체 조회 (List Records)

- **Endpoint:** `GET /records`
- **Description:** 모든 감각 기록 리스트 반환
### 📌 2.2. 감각 기록 전체 조회 (List Records)

- **Endpoint:** `GET /records`
- **Description:** 모든 감각 기록 리스트 반환

- **Query Params (선택):**
  - `sense_type=청각`
  - `location=광화문`

- **Response:**
```json
[
  {
    "id": 17,
    "date": "2025-05-14",
    "location": "광화문",
    "sense_type": "청각",
    "emotion_score": 3,
    "keyword": "종소리",
    "description": "은은한 종소리",
    "image_url": "...",
    "audio_url": "..."
  }
]
```

### 📌 2.3. 단일 기록 조회 (Get Records by ID)

- **Endpoint:** `GET /records/{id}`
- **Description:** 특정 ID의 기록 상세 정보 조회
- **Response:**
```json
{
  "id": 17,
  "date": "2025-05-14",
  "location": "광화문",
  "sense_type": "청각",
  "emotion_score": 3,
  "description": "은은한 종소리",
  "keyword": "조용함, 청각적 경험",
  "image_url": "...",
  "audio_url": "..."
}
```

### 📌 2.4 기록 삭제 (Delete Record)

- **Endpoint:** `DELETE /records/{id}`
- **Description:** 관리자 권한으로 기록 삭제
- **Response:**
```json
{
  "message": "Record deleted"
}
```

## 👤 3. 사용자 인증 API(향후 구현)

### 📌 3.1. 회원가입

- **Endpoint:** `POST /users/signup`
- **Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

- **Response:**
```json
{
  "message": "Signup successful",
  "user_id": 1
}
```







