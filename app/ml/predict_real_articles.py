# app/ml/predict_real_articles.py
from datetime import datetime

from app.db.session import SessionLocal
from app.models.article import Article
from app.ml.inference import predict_article_category


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.clean_summary.isnot(None))
    .order_by(Article.id.desc())
    .limit(10)
    .all()
)

match_count = 0
mismatch_count = 0

for article in articles:
    print()
    print(f"Article ID: {article.id}")
    print(f"Title: {article.title}")

    prediction, confidence = predict_article_category(
        article.clean_summary
    )

    print()
    print(f"Stored Category: {article.ml_category}")
    print(f"Predicted Category: {prediction}")

    if article.ml_category == prediction:
        match_count += 1
    else:
        mismatch_count += 1


    article.ml_category = prediction
    article.ml_confidence = float(confidence)
    article.ml_last_classified_at = datetime.utcnow()

    print()


db.commit()

print()
print("Prediction Summary:")

total_predictions = match_count + mismatch_count

agreement_percentage = (
    (match_count / total_predictions) * 100
    if total_predictions > 0
    else 0
)

print(f"Matches: {match_count}")
print(f"Mismatches: {mismatch_count}")
print(f"Agreement: {agreement_percentage:.1f}%")
