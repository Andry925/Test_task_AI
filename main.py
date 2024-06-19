from fastapi import FastAPI, Request
import uvicorn
from AI_logic.summarizer import run_summarizer

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summary = run_summarizer(text)
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)