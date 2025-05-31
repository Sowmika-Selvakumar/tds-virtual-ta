# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from qa_engine import get_answer

app = FastAPI()

class Query(BaseModel):
    question: str
    image: str = None

@app.post("/api/")
async def virtual_ta(query: Query):
    # Optionally process image here with OCR
    answer_text = get_answer(query.question)
    return {
        "answer": answer_text,
        "links": []  # You can enhance this later
    }
