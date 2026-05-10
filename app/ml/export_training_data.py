# app/ml/export_training_data.py

from app.db.session import SessionLocal
from app.models.article import Article


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.ml_category.isnot(None))
    .limit(20)
    .all()
)

print()
print(f"Articles Loaded: {len(articles)}")

for article in articles:
    print()
    print(f"Category: {article.ml_category}")
    print(f"Title: {article.title}")
