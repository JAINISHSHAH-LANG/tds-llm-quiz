from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class Submission(BaseModel):
    email: str
    secret: str
    url: str
    answer: str

@app.get("/")
def home():
    return {"message": "API is live. Use POST /submit"}

@app.post("/submit")
def submit(data: Submission):
    # Validation example
    if data.answer.strip() == "42":
        return {
            "status": "correct",
            "next": "https://tds-llm-analysis.s-anand.net/project2",
            "message": "Correct answer. Proceed to next step."
        }
    else:
        return {
            "status": "incorrect",
            "message": "Wrong answer. Try again."
        }
