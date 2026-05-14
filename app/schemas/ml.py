from pydantic import BaseModel


class ArticlePredictionRequest(BaseModel):
    text: str


class ArticlePredictionResponse(BaseModel):
    category: str
    confidence: float

