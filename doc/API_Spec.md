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
'''

{
  "message": "Record saved successfully",
  "id": 17
}



