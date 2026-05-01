from datetime import datetime
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.crud.article import create_article, get_articles, count_articles
from app.schemas.article import ArticleCreate, ArticleRead

router = APIRouter()


@router.post("/articles", response_model=ArticleRead)
def create(article: ArticleCreate, db: Session = Depends(get_db)):
    return create_article(db, article)

@router.get("/articles/count")
def article_count(db: Session = Depends(get_db)):
    return {"count": count_articles(db)}

@router.get("/articles", response_model=list[ArticleRead])

# Endpoint
@router.get("/articles", response_model=list[ArticleRead])
def list_all(
#   # Parameters:
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    min_quality_score: float | None = Query(None, ge=0),
    keyword: str | None = Query(None),
    language: str | None = Query(None),
    source_name: str | None = Query(None),
    top_keyword: str | None = Query(None),
    published_after: datetime | None = Query(None),
):

    # CRUD passes
    return get_articles(
        db,
        limit=limit,
        min_quality_score=min_quality_score,
        language=language,
        source_name=source_name,
        top_keyword=top_keyword,
        published_after=published_after,
    )
