from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import requests

app = FastAPI()

# 1. ALLOW THE GRADING SCRIPT TO ACCESS YOUR API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This fulfills the "Access-Control-Allow-Origin: *" rule
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify")
def classify_name(name: str = Query(None)):
    # 2. INPUT VALIDATION
    if name is None or name.strip() == "":
        return Response(
            content='{"status": "error", "message": "Name parameter is required"}',
            status_code=400,
            media_type="application/json"
        )
    
    # FastAPI automatically handles 422 if the input isn't a string-compatible type

    try:
        # 3. CALL EXTERNAL API
        gender_api_url = f"https://api.genderize.io/?name={name}"
        response = requests.get(gender_api_url, timeout=5)
        res_data = response.json()

        # 4. HANDLE EDGE CASES (No prediction or zero count)
        gender = res_data.get("gender")
        count = res_data.get("count", 0)

        if gender is None or count == 0:
            return {
                "status": "error", 
                "message": "No prediction available for the provided name"
            }

        # 5. DATA PROCESSING & CONFIDENCE LOGIC
        probability = res_data.get("probability", 0.0)
        
        # Rule: true if probability >= 0.7 AND sample_size >= 100
        is_confident = (probability >= 0.7) and (count >= 100)
        
        # Current time in ISO 8601 UTC format
        processed_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        # 6. RETURN SUCCESS RESPONSE
        return {
            "status": "success",
            "data": {
                "name": name,
                "gender": gender,
                "probability": probability,
                "sample_size": count, # renamed from 'count'
                "is_confident": is_confident,
                "processed_at": processed_at
            }
        }

    except Exception:
        return Response(
            content='{"status": "error", "message": "Internal Server Error or External API failure"}',
            status_code=500,
            media_type="application/json"
        )
