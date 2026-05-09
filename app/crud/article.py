# app/crud/article.py
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate


# signature / create_article() Function DEFINITION
def create_article(db: Session, article: ArticleCreate) -> Article:
    existing = get_article_by_url(db, article.url)
    if existing:
        return existing

    article_data = article.model_dump()
    article_data.pop("search_vector", None)

    db_article = Article(**article_data)

    title_vector = func.setweight(
        func.to_tsvector(
            "english",
            article_data.get("title") or "",
        ),
        "A",
    )

    keywords_vector = func.setweight(
        func.to_tsvector(
            "english",
            article_data.get("keywords") or "",
        ),
        "B",
    )

    summary_vector = func.setweight(
        func.to_tsvector(
            "english",
            article_data.get("clean_summary") or "",
        ),
        "C",
    )

    db_article.search_vector = (
        title_vector
        .op("||")(keywords_vector)
        .op("||")(summary_vector)
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


# signature / build_article_query() Function DEFINITION
def build_article_query(
    db: Session,
    min_quality_score: float | None = None,
    keyword: str | None = None,
    language: str | None = None,
    source_name: str | None = None,
    top_keyword: str | None = None,
    published_after: datetime | None = None,
    published_before: datetime | None = None,
    has_keywords: bool | None = None,
    has_summary: bool | None = None,
    has_language: bool | None = None,
    has_top_keyword: bool | None = None,
    has_quality_score: bool | None = None,
    min_token_count: int | None = None,
    max_token_count: int | None = None,
    min_char_count: int | None = None,
    max_char_count: int | None = None,
    min_word_count: int | None = None,
    max_word_count: int | None = None,
    search: str | None = None,
    search_title: str | None = None,
    search_summary: str | None = None,
    search_keywords: str | None = None,
    search_source: str | None = None,
    search_all: str | None = None,
    exclude_keyword: str | None = None,
    exclude_source: str | None = None,
    exclude_language: str | None = None,
):
    query = db.query(Article)

    ### Quality / Inclusion Filters
    if min_quality_score is not None:
        query = query.filter(Article.quality_score >= min_quality_score)
    if keyword:
        query = query.filter(Article.keywords.ilike(f"%{keyword}%"))
    if language:
        query = query.filter(Article.language == language)
    if source_name:
        query = query.filter(Article.source_name.ilike(f"%{source_name}%"))
    if top_keyword:
        query = query.filter(Article.top_keyword.ilike(f"%{top_keyword}%"))

    ### Date Filters
    if published_after:
        query = query.filter(Article.published_at >= published_after)
    if published_before:
        query = query.filter(Article.published_at <= published_before)

    if has_keywords is True:
        query = query.filter(Article.keywords.isnot(None))
    if has_keywords is False:
        query = query.filter(Article.keywords.is_(None))
    if has_summary is True:
        query = query.filter(Article.clean_summary.isnot(None))
    if has_summary is False:
        query = query.filter(Article.clean_summary.is_(None))
    if has_language is True:
        query = query.filter(Article.language.isnot(None))
    if has_language is False:
        query = query.filter(Article.language.is_(None))
    if has_top_keyword is True:
        query = query.filter(Article.top_keyword.isnot(None))
    if has_top_keyword is False:
        query = query.filter(Article.top_keyword.is_(None))
    if has_quality_score is True:
        query = query.filter(Article.quality_score.isnot(None))
    if has_quality_score is False:
        query = query.filter(Article.quality_score.is_(None))

    ### Count / Length Filters
    if min_token_count is not None:
        query = query.filter(Article.token_count >= min_token_count)
    if max_token_count is not None:
        query = query.filter(Article.token_count <= max_token_count)
    if min_char_count is not None:
        query = query.filter(Article.char_count >= min_char_count)
    if max_char_count is not None:
        query = query.filter(Article.char_count <= max_char_count)
    if min_word_count is not None:
        query = query.filter(Article.word_count >= min_word_count)
    if max_word_count is not None:
        query = query.filter(Article.word_count <= max_word_count)

    ### Search Filters
    if search:
        query = query.filter(
            Article.search_vector.op("@@")(
                func.plainto_tsquery("english", search)
            )
        )
    if search_title:
        query = query.filter(Article.title.ilike(f"%{search_title}%"))
    if search_summary:
        query = query.filter(Article.clean_summary.ilike(f"%{search_summary}%"))
    if search_keywords:
        query = query.filter(Article.keywords.ilike(f"%{search_keywords}%"))
    if search_source:
        query = query.filter(Article.source_name.ilike(f"%{search_source}%"))
    if search_all:
        term = f"%{search_all}%"
        query = query.filter(
            (Article.title.ilike(term))
            | (Article.clean_summary.ilike(term))
            | (Article.keywords.ilike(term))
            | (Article.source_name.ilike(term))
        )

    ### Exclusion Filters
    if exclude_keyword:
        query = query.filter(~Article.keywords.ilike(f"%{exclude_keyword}%"))
    if exclude_source:
        query = query.filter(~Article.source_name.ilike(f"%{exclude_source}%"))
    if exclude_language:
        query = query.filter(Article.language != exclude_language)

    return query

### Function get_articles() DEFINITION
def get_articles(
    ### Parameters:
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
    min_char_count: int | None = None,
    max_char_count: int | None = None,
    min_word_count: int | None = None,
    max_word_count: int | None = None,
    search: str | None = None,
    search_title: str | None = None,
    search_summary: str | None = None,
    search_keywords: str | None = None,
    search_source: str | None = None,
    search_all: str | None = None,
    exclude_keyword: str | None = None,
    exclude_source: str | None = None,
    exclude_language: str | None = None,
    page: int | None = None,
) -> list[Article]:

    # get_articles() FUNCTION CALL to build_articles_query()
    query = build_article_query(
        db,
        min_quality_score=min_quality_score,
        keyword=keyword,
        language=language,
        source_name=source_name,
        top_keyword=top_keyword,
        published_after=published_after,
        published_before=published_before,
        has_keywords=has_keywords,
        has_summary=has_summary,
        has_language=has_language,
        has_top_keyword=has_top_keyword,
        has_quality_score=has_quality_score,
        min_token_count=min_token_count,
        max_token_count=max_token_count,
        min_char_count=min_char_count,
        max_char_count=max_char_count,
        min_word_count=min_word_count,
        max_word_count=max_word_count,
        search=search,
        search_title=search_title,
        search_summary=search_summary,
        search_keywords=search_keywords,
        search_source=search_source,
        search_all=search_all,
        exclude_keyword=exclude_keyword,
        exclude_source=exclude_source,
        exclude_language=exclude_language,
    )

    ### ### ###  Filters
    ### Sorting Filters
    # Rank Branch
    if search and sort_by == "rank":

        rank = func.ts_rank_cd(
            Article.search_vector,
            func.plainto_tsquery("english", search),
            32,
        ).label("rank")

        query = query.order_by(rank.desc())

        if page and page > 1:
            offset = (page - 1) * limit
            query = query.offset(offset)

        results = (
            query
            .add_columns(rank)
            .limit(limit)
            .all()
        )

        articles = []

        for article, rank_value in results:
            article.rank = rank_value
            articles.append(article)

        return articles

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

    if page and page > 1:
        offset = (page - 1) * limit
        query = query.offset(offset)

    ### Limit / Return for the rank branch
    return query.limit(limit).all()


#################################
def get_article_by_url(db: Session, url: str) -> Article | None:
    return db.query(Article).filter(Article.url == url).first()

# signature / Function DEFINITION
def count_filtered_articles(
    db: Session,
    min_quality_score: float | None = None,
    keyword: str | None = None,
    language: str | None = None,
    source_name: str | None = None,
    top_keyword: str | None = None,
    published_after: datetime | None = None,
    published_before: datetime | None = None,
    has_keywords: bool | None = None,
    has_summary: bool | None = None,
    has_language: bool | None = None,
    has_top_keyword: bool | None = None,
    has_quality_score: bool | None = None,
    min_token_count: int | None = None,
    max_token_count: int | None = None,
    min_char_count: int | None = None,
    max_char_count: int | None = None,
    min_word_count: int | None = None,
    max_word_count: int | None = None,
    search: str | None = None,
    search_title: str | None = None,
    search_summary: str | None = None,
    search_keywords: str | None = None,
    search_source: str | None = None,
    search_all: str | None = None,
    exclude_keyword: str | None = None,
    exclude_source: str | None = None,
    exclude_language: str | None = None,
) -> int:
    # FUNCTION CALL to build_article_query()
    query = build_article_query(
        db,
        min_quality_score=min_quality_score,
        keyword=keyword,
        language=language,
        source_name=source_name,
        top_keyword=top_keyword,
        published_after=published_after,
        published_before=published_before,
        has_keywords=has_keywords,
        has_summary=has_summary,
        has_language=has_language,
        has_top_keyword=has_top_keyword,
        has_quality_score=has_quality_score,
        min_token_count=min_token_count,
        max_token_count=max_token_count,
        min_char_count=min_char_count,
        max_char_count=max_char_count,
        min_word_count=min_word_count,
        max_word_count=max_word_count,
        search=search,
        search_title=search_title,
        search_summary=search_summary,
        search_keywords=search_keywords,
        search_source=search_source,
        search_all=search_all,
        exclude_keyword=exclude_keyword,
        exclude_source=exclude_source,
        exclude_language=exclude_language,
    )
    return query.count()

def count_articles(db: Session) -> int:
    return db.query(Article).count()

