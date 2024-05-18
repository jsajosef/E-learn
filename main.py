from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

# Your OpenAI API key
OPENAI_API_KEY = 'put_your_openai_api_key'
openai.api_key = OPENAI_API_KEY

class TopicRequest(BaseModel):
    topic: str

@app.post("/explain/")
async def explain_topic(request: TopicRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Explain the following topic in detail: {request.topic}",
            max_tokens=500
        )
        explanation = response.choices[0].text.strip()
        return {"explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))