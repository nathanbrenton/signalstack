# Semantic article similarity retrieval.
from sklearn.metrics.pairwise import cosine_similarity
from app.models.article import Article


def find_similar_articles(
    db,
    article_id: int,
    limit: int = 5,
    min_similarity: float = 0.0,
) -> list[tuple[Article, float]]:
    """
    Find semantically similar articles.
    """

    base_article = db.get(
        Article,
        article_id,
    )

    if (
        not base_article
        or not base_article.embedding
    ):
        return []

    candidate_articles = (
        db.query(Article)
        .filter(Article.id != article_id)
        .filter(Article.embedding.isnot(None))
        .limit(100)
        .all()
    )

    similarity_results = []

    for article in candidate_articles:

        similarity = cosine_similarity(
            [base_article.embedding],
            [article.embedding],
        )[0][0]

        if similarity < min_similarity:
            continue

        similarity_results.append(
            (
                article,
                float(similarity),
            )
        )

    similarity_results.sort(
        key=lambda result: result[1],
        reverse=True,
    )

    return similarity_results[:limit]
