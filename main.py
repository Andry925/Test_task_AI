from fastapi import FastAPI, Request
import uvicorn
from langchain import SimpleSummarizer

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summarizer = SimpleSummarizer()
    summary = summarizer.summarize(text)
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)