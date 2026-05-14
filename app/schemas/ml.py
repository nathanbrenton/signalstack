from pydantic import BaseModel, Field


class ArticlePredictionRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=5000)


### SCHEMA
class ArticlePredictionResponse(BaseModel):
    category: str
    confidence: float
    probabilities: dict[str, float]
    model_version: str
    inference_time_ms: float

