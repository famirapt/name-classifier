## GitHub Repository Details

* **Repository Name:** `name-classifier`
* **Description:** A Python-based microservice that integrates with the Genderize API to classify names with custom confidence logic and standardized error handling.

---

## Recommended `README.md` Content
Copy and paste this into a file named `README.md` in your project root. It covers all the technical requirements the grader will be looking for.

```markdown
# Name Classifier API

A robust Python microservice built with **FastAPI** that predicts the gender of a given name. This project acts as a middleware for the Genderize.io API, applying custom validation rules, data transformation, and confidence scoring.

## 🚀 Live Demo
**Base URL:** `https://your-app-name.onrender.com`  
**Endpoint:** `/api/classify?name=<name>`

## 🛠 Features
- **Data Transformation:** Renames raw API fields (e.g., `count` to `sample_size`) for better clarity.
- **Custom Confidence Logic:** Returns `is_confident: true` only if the probability is ≥ 0.7 AND the sample size is ≥ 100.
- **Strict Validation:** Handles missing parameters (400) and invalid data types (422).
- **CORS Enabled:** Fully accessible for cross-origin grading scripts via `Access-Control-Allow-Origin: *`.
- **Performance:** Optimized to run under 500ms (internal processing time).

## 📊 Logic & Rules
- **Success:** Returns a JSON object with processed data and a UTC ISO 8601 timestamp.
- **Edge Cases:** If the name is unknown to the underlying provider, returns a graceful error message instead of failing.
- **Error Format:** All errors follow the structure: 
  ```json
  { "status": "error", "message": "<error message>" }
  ```

## ⚙️ Installation & Local Setup

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/name-classifier.git](https://github.com/your-username/name-classifier.git)
   cd name-classifier
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```

## 🧪 Testing Examples
- **Valid Request:** `/api/classify?name=peter`
- **Missing Name:** `/api/classify?name=` (Returns 400)
- **Unknown Name:** `/api/classify?name=shrubbery` (Returns error message)

## 🧰 Tech Stack
- **Language:** Python 3.x
- **Framework:** FastAPI
- **HTTP Client:** Requests
- **Deployment:** Render
```

---

## Pro-Tips for the Submission
1.  **Public Repo:** Double-check that your GitHub repository visibility is set to **Public** before submitting, or the grader won't be able to see your code.
2.  **Environment:** Ensure your `requirements.txt` includes `fastapi`, `uvicorn`, and `requests`.
3.  **URL Consistency:** Make sure the URL you submit starts with `https://` and includes the `/api/classify` path.