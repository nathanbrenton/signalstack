# Semantic search using embedding similarity.

from sklearn.metrics.pairwise import cosine_similarity

from app.ml.embeddings import generate_embedding
from app.models.article import Article


def semantic_search(
    db,
    query: str,
    limit: int = 5,
    min_similarity: float = 0.0,
):
    """
    Perform semantic article search.
    """

    query_embedding = generate_embedding(
        query
    )

    candidate_articles = (
        db.query(Article)
        .filter(Article.embedding.isnot(None))
        .limit(100)
        .all()
    )

    results = []

    for article in candidate_articles:

        similarity = cosine_similarity(
            [query_embedding],
            [article.embedding],
        )[0][0]

        if similarity < min_similarity:
            continue

        results.append(
            (
                article,
                float(similarity),
            )
        )

    results.sort(
        key=lambda result: result[1],
        reverse=True,
    )

    return results[:limit]
