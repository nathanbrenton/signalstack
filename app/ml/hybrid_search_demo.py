# Hybrid retrieval ranking demo.

from sklearn.metrics.pairwise import cosine_similarity

from app.db.session import SessionLocal
from app.ml.embeddings import generate_embedding
from app.models.article import Article


db = SessionLocal()

query = "virus outbreak on cruise ship"

query_embedding = generate_embedding(
    query
)

articles = (
    db.query(Article)
    .filter(Article.embedding.isnot(None))
    .limit(25)
    .all()
)

results = []

for article in articles:

    semantic_similarity = cosine_similarity(
        [query_embedding],
        [article.embedding],
    )[0][0]

    ml_confidence = (
        article.ml_confidence or 0.0
    )

    hybrid_score = (
        semantic_similarity * 0.8
    ) + (
        ml_confidence * 0.2
    )

    results.append(
        {
            "article": article,
            "semantic_similarity": semantic_similarity,
            "ml_confidence": ml_confidence,
            "hybrid_score": hybrid_score,
        }
    )

results.sort(
    key=lambda result: result["hybrid_score"],
    reverse=True,
)

print()
print("Hybrid Retrieval Results")
print()

for result in results[:10]:

    article = result["article"]

    print("--------------------------------")
    print(article.title)

    print(
        f"Semantic Similarity: "
        f"{result['semantic_similarity']:.4f}"
    )

    print(
        f"ML Confidence: "
        f"{result['ml_confidence']:.4f}"
    )

    print(
        f"Hybrid Score: "
        f"{result['hybrid_score']:.4f}"
    )
