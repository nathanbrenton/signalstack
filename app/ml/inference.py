# app/ml/inference.py

import joblib

MODEL_VERSION = "1.0"


# Persisted ML artifacts
classifier = joblib.load(
    "app/ml/models/article_classifier.joblib"
)

vectorizer = joblib.load(
    "app/ml/models/article_vectorizer.joblib"
)



def predict_article_category(
    text: str,
) -> tuple[str, float]:
    """
    Predict the highest-quality article category.
    """

    document_matrix = vectorizer.transform([text])

    prediction = classifier.predict(
        document_matrix
    )[0]

    probabilities = classifier.predict_proba(
        document_matrix
    )[0]

    confidence = max(probabilities)

    return prediction, float(confidence)



def predict_article_probabilities(
    text: str,
) -> dict[str, float]:
    """
    Return probability scores for all article categories.
    """

    document_matrix = vectorizer.transform([text])

    probabilities = classifier.predict_proba(
        document_matrix
    )[0]

    probability_map = {}

    for category, probability in zip(
        classifier.classes_,
        probabilities,
    ):
        probability_map[category] = float(probability)

    return probability_map
