from pydantic import BaseModel, Field


class ArticlePredictionRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=5000)


class ArticlePredictionResponse(BaseModel):
    category: str
    confidence: float

