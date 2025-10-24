from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="AI Text Summarizer")

# Load summarization model
summarizer = pipeline("summarization")

# Define request body
class TextRequest(BaseModel):
    text: str

# POST endpoint
@app.post("/summarize")
def summarize_text(request: TextRequest):
    summary = summarizer(
        request.text,
        max_length=100,
        min_length=20,
        do_sample=False
    )
    return {"summary": summary[0]['summary_text']}
