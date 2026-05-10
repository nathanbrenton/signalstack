# app/ml/predict_article.py

import joblib


classifier = joblib.load(
    "app/ml/models/article_classifier.joblib"
)

vectorizer = joblib.load(
    "app/ml/models/article_vectorizer.joblib"
)


documents = [
    "Artificial intelligence systems automate cybersecurity analysis",
    "The baseball team won the championship series",
    "Congress debated a new economic policy bill",
]


document_matrix = vectorizer.transform(documents)

predictions = classifier.predict(document_matrix)

prediction_probabilities = classifier.predict_proba(
    document_matrix
)


for document, prediction, probabilities in zip(
    documents,
    predictions,
    prediction_probabilities,
):
    print()
    print(f"Document: {document}")
    print(f"Prediction: {prediction}")

    print("Confidence Scores:")

    for category, probability in zip(
        classifier.classes_,
        probabilities,
    ):
        print(f"  {category}: {probability:.3f}")
