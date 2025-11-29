import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# FastAPI app
api = FastAPI()

# Enable CORS
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Submission schema
class Submission(BaseModel):
    email: str
    secret: str
    url: str
    answer: str

@api.get("/")
def home():
    return {"message": "API is live. Use POST /submit"}

@api.post("/submit")
def submit(data: Submission):
    if data.answer.strip() == "42":
        return {
            "status": "correct",
            "next": "https://tds-llm-analysis.s-anand.net/project2"
        }
    else:
        return {"status": "incorrect"}

# Gradio placeholder UI
def placeholder(x):
    return "This is an API space. Use /submit endpoint."

demo = gr.Interface(fn=placeholder, inputs="text", outputs="text")

# Mount Gradio in FastAPI
app = gr.mount_gradio_app(api, demo, path="/")

