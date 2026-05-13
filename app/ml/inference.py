# app/ml/inference.py

import joblib


classifier = joblib.load(
    "app/ml/models/article_classifier.joblib"
)

vectorizer = joblib.load(
    "app/ml/models/article_vectorizer.joblib"
)


def predict_article_category(
    text: str,
) -> tuple[str, float]:

    document_matrix = vectorizer.transform([text])

    prediction = classifier.predict(
        document_matrix
    )[0]

    probabilities = classifier.predict_proba(
        document_matrix
    )[0]

    confidence = max(probabilities)

    return prediction, float(confidence)

