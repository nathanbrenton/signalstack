from fastapi import APIRouter, Depends
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
def list_all(db: Session = Depends(get_db)):
    return get_articles(db)
