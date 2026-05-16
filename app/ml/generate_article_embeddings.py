# Generate semantic embeddings for articles.

from app.db.session import SessionLocal
from app.models.article import Article
from app.ml.embeddings import generate_embedding


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.summary.isnot(None))
    .filter(Article.embedding.is_(None))
    .limit(25)
    .all()
)

print()
print("Articles Loaded:")
print(len(articles))

updated_count = 0

for article in articles:

    embedding = generate_embedding(
        article.summary
    )

    article.embedding = embedding

    updated_count += 1

    print(
        f"Embedded Article ID: {article.id}"
    )

db.commit()

print()
print("Embedding Backfill Complete")
print(
    f"Articles Updated: {updated_count}"
)
