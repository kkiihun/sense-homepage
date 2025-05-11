// components/UploadForm.tsx
import { useState } from "react";

export default function UploadForm() {
  const [form, setForm] = useState({
    date: "",
    location: "",
    sense_type: "",
    keyword: "",
    emotion_score: "",
    description: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/upload", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    if (res.ok) {
      alert("성공적으로 업로드되었습니다!");
      setForm({ date: "", location: "", sense_type: "", keyword: "", emotion_score: "", description: "" });
    } else {
      alert("업로드 실패");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 bg-gray-100 p-6 rounded shadow">
      <input type="date" name="date" value={form.date} onChange={handleChange} placeholder="날짜 (YYYY-MM-DD)" className="input" required />
      <input name="location" value={form.location} onChange={handleChange} placeholder="장소" className="input" required />
      <input name="sense_type" value={form.sense_type} onChange={handleChange} placeholder="감각유형 (예: 맛, 향)" className="input" required />
      <input name="keyword" value={form.keyword} onChange={handleChange} placeholder="키워드" className="input" />
      <input name="emotion_score" value={form.emotion_score} onChange={handleChange} placeholder="감정점수 (-5 ~ 5)" type="number" className="input" />
      <textarea name="description" value={form.description} onChange={handleChange} placeholder="감정 설명" className="input" />
      <button type="submit" className="bg-orange-500 text-white px-4 py-2 rounded">등록</button>
    </form>
  );
}
