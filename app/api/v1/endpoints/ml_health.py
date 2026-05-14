from fastapi import APIRouter
from pathlib import Path

from app.ml.inference import MODEL_VERSION


router = APIRouter()


@router.get("/ml/health")
def ml_health():

    classifier_exists = Path(
        "app/ml/models/article_classifier.joblib"
    ).exists()

    vectorizer_exists = Path(
        "app/ml/models/article_vectorizer.joblib"
    ).exists()

    return {
        "status": "ok",
        "model_version": MODEL_VERSION,
        "classifier_loaded": classifier_exists,
        "vectorizer_loaded": vectorizer_exists,
    }
