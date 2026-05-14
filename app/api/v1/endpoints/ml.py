from fastapi import APIRouter

from app.ml.inference import (
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
    category, confidence = predict_article_category(
        request.text
    )

    probabilities = predict_article_probabilities(
        request.text
    )

    ### RETURN BLOCK
    return {
        "category": category,
        "confidence": confidence,
        "probabilities": probabilities,
    }
