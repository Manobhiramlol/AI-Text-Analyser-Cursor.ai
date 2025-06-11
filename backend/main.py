from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class TextRequest(BaseModel):
    text: str

class AnalysisResult(BaseModel):
    summary: str
    sentiment: str
    key_points: List[str]
    word_count: int
    reading_time: str

@app.post("/api/analyze", response_model=AnalysisResult)
async def analyze_text(request: TextRequest):
    try:
        # Calculate basic metrics
        word_count = len(request.text.split())
        reading_time_mins = max(1, round(word_count / 200))  # Assuming 200 words per minute
        reading_time = f"{reading_time_mins} min{'s' if reading_time_mins > 1 else ''}"

        # Get AI analysis
        response = await openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that analyzes text and provides summaries, sentiment analysis, and key points. Respond with JSON only."
                },
                {
                    "role": "user",
                    "content": f"Analyze the following text and provide a summary, sentiment analysis, and key points: {request.text}"
                }
            ],
            response_format={"type": "json_object"}
        )

        # Parse the response
        result = response.choices[0].message.content
        analysis = eval(result)  # Convert string to dict

        return AnalysisResult(
            summary=analysis.get("summary", "No summary available"),
            sentiment=analysis.get("sentiment", "Neutral"),
            key_points=analysis.get("key_points", []),
            word_count=word_count,
            reading_time=reading_time
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 