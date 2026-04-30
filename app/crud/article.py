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


#def get_articles(db: Session) -> list[Article]:
#    return db.query(Article).all()
def get_articles(db: Session) -> list[Article]:
    return (
        db.query(Article)
        .order_by(Article.quality_score.desc().nullslast())
        .all()
    )


def get_article_by_url(db: Session, url: str) -> Article | None:
    return db.query(Article).filter(Article.url == url).first()

def count_articles(db: Session) -> int:
    return db.query(Article).count()

