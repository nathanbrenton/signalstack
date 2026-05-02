from datetime import datetime
from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate


def create_article(db: Session, article: ArticleCreate) -> Article:
    existing = get_article_by_url(db, article.url)
    if existing:
        return existing

    db_article = Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(
##### Parameters:
    db: Session,
    limit: int = 10,
    min_quality_score: float | None = None,
    keyword: str | None = None,
    language: str | None = None,
    source_name: str | None = None,
    top_keyword: str | None = None,
    published_after: datetime | None = None,
    published_before: datetime | None = None,
    sort_by: str | None = None,
    order: str | None = None,
    has_keywords: bool | None = None,
    has_summary: bool | None = None,
    has_language: bool | None = None,
    has_top_keyword: bool | None = None,
    has_quality_score: bool | None = None,
    min_token_count: int | None = None,
    max_token_count: int | None = None,
) -> list[Article]:
    query = db.query(Article)

    if min_quality_score is not None:
        query = query.filter(Article.quality_score >= min_quality_score)

#   # Filters
    if keyword:
        query = query.filter(Article.keywords.ilike(f"%{keyword}%"))

    if language:
        query = query.filter(Article.language == language)

    if source_name:
        query = query.filter(Article.source_name.ilike(f"%{source_name}%"))

    if top_keyword:
        query = query.filter(Article.top_keyword.ilike(f"%{top_keyword}%"))

    if published_after:
        query = query.filter(Article.published_at >= published_after)

    if published_before:
        query = query.filter(Article.published_at <= published_before)


    if sort_by == "published_at":
        if order == "asc":
            query = query.order_by(Article.published_at.asc().nullslast())
        else:
            query = query.order_by(Article.published_at.desc().nullslast())
    else:
        if order == "asc":
            query = query.order_by(Article.quality_score.asc().nullslast())
        else:
            query = query.order_by(Article.quality_score.desc().nullslast())
    return query.limit(limit).all()

    if has_keywords is True:
        query = query.filter(Article.keywords.isnot(None))

    if has_summary is True:
        query = query.filter(Article.clean_summary.isnot(None))

    if has_language is True:
        query = query.filter(Article.language.isnot(None))

    if has_top_keyword is True:
        query = query.filter(Article.top_keyword.isnot(None))

    if has_quality_score is True:
        query = query.filter(Article.quality_score.isnot(None))

    if min_token_count is not None:
        query = query.filter(Article.token_count >= min_token_count)

    if max_token_count is not None:
        query = query.filter(Article.token_count <= max_token_count)
#################################
def get_article_by_url(db: Session, url: str) -> Article | None:
    return db.query(Article).filter(Article.url == url).first()


def count_articles(db: Session) -> int:
    return db.query(Article).count()

