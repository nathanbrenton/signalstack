# app/ml/predict_real_articles.py

import joblib

from app.db.session import SessionLocal
from app.models.article import Article


classifier = joblib.load(
    "app/ml/models/article_classifier.joblib"
)

vectorizer = joblib.load(
    "app/ml/models/article_vectorizer.joblib"
)


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.clean_summary.isnot(None))
    .order_by(Article.id.desc())
    .limit(10)
    .all()
)


documents = [
    article.clean_summary
    for article in articles
]


document_matrix = vectorizer.transform(documents)

predictions = classifier.predict(document_matrix)

prediction_probabilities = classifier.predict_proba(
    document_matrix
)


for article, prediction, probabilities in zip(
    articles,
    predictions,
    prediction_probabilities,
):
    print()
    print(f"Article ID: {article.id}")
    print(f"Title: {article.title}")

    print()
    print(f"Stored Category: {article.ml_category}")
    print(f"Predicted Category: {prediction}")

    print()
    print("Confidence Scores:")

    for category, probability in zip(
        classifier.classes_,
        probabilities,
    ):
        print(f"  {category}: {probability:.3f}")
