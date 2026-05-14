from fastapi import APIRouter

from app.ml.inference import predict_article_category
from app.schemas.ml import (
    ArticlePredictionRequest,
    ArticlePredictionResponse,
)


router = APIRouter()


@router.post(
    "/ml/predict",
    response_model=ArticlePredictionResponse,
)
def predict(
    request: ArticlePredictionRequest,
):
    category, confidence = predict_article_category(
        request.text
    )

    return {
        "category": category,
        "confidence": confidence,
    }
