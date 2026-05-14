# endpoints/m1.py
# Purpose: defines the RESPONSE STRUCTURE
import time
from fastapi import APIRouter

from app.ml.inference import (
    MODEL_VERSION,
    predict_article_category,
    predict_article_probabilities,
)

from app.schemas.ml import (
    ArticlePredictionRequest,
    ArticlePredictionResponse,
)


router = APIRouter()

# FYI: ENDPOINT = DECORATOR + Function DEFINITION
# DECORATOR (metadata attached to the function)
@router.post(
    "/ml/predict",
    response_model=ArticlePredictionResponse,
)

### python Function DEFINITION  ENDPOINT
def predict(
    request: ArticlePredictionRequest,
):
    start_time = time.perf_counter()

    category, confidence = predict_article_category(
        request.text
    )

    probabilities = predict_article_probabilities(
        request.text
    )

    elapsed_ms = (
        time.perf_counter() - start_time
    ) * 1000

    ### RETURN DICTIONARY BLOCK
    return {
        "category": category,
        "confidence": confidence,
        "probabilities": probabilities,
        "model_version": MODEL_VERSION,
        "inference_time_ms": round(elapsed_ms, 3),
    }
