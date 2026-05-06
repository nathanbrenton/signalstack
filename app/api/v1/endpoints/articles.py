from datetime import datetime
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.crud.article import (
    create_article,
    get_articles,
    count_articles,
    count_filtered_articles,
)
from app.schemas.article import (
    ArticleCreate,
    ArticleRead,
    ArticleListResponse,
)

router = APIRouter()


@router.post("/articles", response_model=ArticleRead)
def create(article: ArticleCreate, db: Session = Depends(get_db)):
    return create_article(db, article)

@router.get("/articles/count")
def article_count(db: Session = Depends(get_db)):
    return {"count": count_articles(db)}


# Endpoint
#@router.get("/articles", response_model=list[ArticleRead])
@router.get("/articles", response_model=ArticleListResponse)

# The list_all Function DEFINITION
def list_all(

##### Parameters (with type annotations):
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    min_quality_score: float | None = Query(None, ge=0),
    keyword: str | None = Query(None),
    language: str | None = Query(None),
    source_name: str | None = Query(None),
    top_keyword: str | None = Query(None),
    published_after: datetime | None = Query(None),
    published_before: datetime | None = Query(None),
    sort_by: str | None = Query(None),
    order: str | None = Query(None),
    has_keywords: bool | None = Query(None),
    has_summary: bool | None = Query(None),
    has_language: bool | None = Query(None),
    has_top_keyword: bool | None = Query(None),
    has_quality_score: bool | None = Query(None),
    min_token_count: int | None = Query(None, ge=0),
    max_token_count: int | None = Query(None, ge=0),
    min_char_count: int | None = Query(None, ge=0),
    max_char_count: int | None = Query(None, ge=0),
    min_word_count: int | None = Query(None, ge=0),
    max_word_count: int | None = Query(None, ge=0),
    search: str | None = Query(None),
    search_title: str | None = Query(None),
    search_summary: str | None = Query(None),
    search_keywords: str | None = Query(None),
    search_source: str | None = Query(None),
    search_all: str | None = Query(None),
    exclude_keyword: str | None = Query(None),
    exclude_source: str | None = Query(None),
    exclude_language: str | None = Query(None),
    page: int | None = Query(None, ge=1),
):


##### CRUD passes
    # The "get_articles" Function CALL:
    articles = get_articles(
        db,
        limit=limit,
        min_quality_score=min_quality_score,
        language=language,
        source_name=source_name,
        top_keyword=top_keyword,
        published_after=published_after,
        published_before=published_before,
        sort_by=sort_by,
        order=order,
        keyword=keyword,
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
        page=page,
    )

    # Function CALL to count_filtered_articles()
    total = count_filtered_articles(
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
    pages = (total + limit - 1) // limit

#    return articles
    return {
        "data": articles,
        "meta": {
            "page": page or 1,
            "limit": limit,
            "total": total,
            "pages": pages,
        },
    }



