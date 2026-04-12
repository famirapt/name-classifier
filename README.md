
---

# 📛 Name Classifier API

A high-performance **Python microservice** built with **FastAPI** that predicts gender based on names. This API acts as an intelligent middleware for Genderize.io, implementing custom data validation and strict confidence scoring.

## 🚀 Quick Links
- **Base URL:** `https://your-app-name.onrender.com`
- **Endpoint:** `/api/classify?name=peter`

## 🧠 Why Use This API?
Recruiters and developers value reliability. This service improves upon raw data by adding:
- **Smart Confidence Scoring:** Only marks a result as `confident` if it meets a high probability (≥ 0.7) and a significant sample size (≥ 100).
- **Data Enrichment:** Transforms raw API responses into clean, descriptive JSON with UTC timestamps.
- **Robust Error Handling:** Specifically handles edge cases, unknown names, and missing parameters with standard HTTP status codes (400, 422).
- **Sub-500ms Performance:** Optimized for high-speed internal processing.

## 🛠️ Tech Stack
- **Backend:** Python 3.x, FastAPI, Uvicorn
- **Integration:** Requests (Genderize.io API)
- **Deployment:** Render (CORS enabled for cross-origin access)

## 💻 Local Setup

1. **Clone & Enter:**
   ```bash
   git clone https://github.com/your-username/name-classifier.git
   cd name-classifier
   ```

2. **Install:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch:**
   ```bash
   uvicorn main:app --reload
   ```

## 🔍 API Logic at a Glance
- **Confident Result:** `probability >= 0.7` AND `sample_size >= 100`.
- **Standardized Errors:**
  ```json
  { "status": "error", "message": "The name provided is invalid or missing." }
  ```