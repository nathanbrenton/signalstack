# Semantic similarity demo using real articles.

from app.db.session import SessionLocal
from app.models.article import Article
from app.ml.embeddings import calculate_similarity


db = SessionLocal()

articles = (
    db.query(Article)
    .filter(Article.summary.isnot(None))
    .limit(5)
    .all()
)

print()
print("Loaded Articles:")
print(len(articles))

print()

base_article = articles[0]

print("Base Article:")
print(base_article.title)

print()

for article in articles[1:]:

    similarity = calculate_similarity(
        base_article.summary,
        article.summary,
    )

    print("-----------------------------------")
    print(article.title)

    print(
        f"Similarity: {similarity:.4f}"
    )
