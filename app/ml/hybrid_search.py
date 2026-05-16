# Hybrid semantic retrieval service.

from sklearn.metrics.pairwise import cosine_similarity

from app.ml.embeddings import generate_embedding
from app.models.article import Article


def hybrid_search(
    db,
    query: str,
    limit: int = 5,
    min_similarity: float = 0.0,
):
    """
    Perform hybrid semantic retrieval.
    """

    query_embedding = generate_embedding(
        query
    )

    articles = (
        db.query(Article)
        .filter(Article.embedding.isnot(None))
        .limit(100)
        .all()
    )

    results = []

    for article in articles:

        semantic_similarity = cosine_similarity(
            [query_embedding],
            [article.embedding],
        )[0][0]

        if semantic_similarity < min_similarity:
            continue

        ml_confidence = (
            article.ml_confidence or 0.0
        )

        hybrid_score = (
            semantic_similarity * 0.8
        ) + (
            ml_confidence * 0.2
        )

        results.append(
            (
                article,
                {
                    "semantic_similarity":
                        float(
                            semantic_similarity
                        ),
                    "ml_confidence":
                        float(ml_confidence),
                    "hybrid_score":
                        float(hybrid_score),
                },
            )
        )

    results.sort(
        key=lambda result:
            result[1]["hybrid_score"],
        reverse=True,
    )

    return results[:limit]
