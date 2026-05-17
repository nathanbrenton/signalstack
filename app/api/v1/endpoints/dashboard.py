from sqlalchemy import func
from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends

from app.db.deps import get_db
from app.models.article import Article
from app.models.rss_feed_source import RSSFeedSource

from sqlalchemy import desc

router = APIRouter()


@router.get("/dashboard/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db),
):
    total_articles = (
        db.query(func.count(Article.id))
        .scalar()
    )

    active_rss_feeds = (
        db.query(func.count(RSSFeedSource.id))
        .filter(RSSFeedSource.is_active.is_(True))
        .scalar()
    )

    ml_classified_articles = (
        db.query(func.count(Article.id))
        .filter(Article.ml_category.isnot(None))
        .scalar()
    )

    embedded_articles = (
        db.query(func.count(Article.id))
        .filter(Article.embedding.isnot(None))
        .scalar()
    )

    latest_article = (
        db.query(Article)
        .order_by(desc(Article.ingested_at))
        .first()
    )

    latest_feed_ingest = (
        db.query(RSSFeedSource)
        .filter(
            RSSFeedSource.last_ingested_at.isnot(None)
        )
        .order_by(desc(RSSFeedSource.last_ingested_at))
        .first()
    )

    return {
        "total_articles": total_articles,
        "active_rss_feeds": active_rss_feeds,
        "ml_classified_articles": ml_classified_articles,
        "embedded_articles": embedded_articles,
        "last_article_ingested_at": (
            latest_article.ingested_at
            if latest_article
            else None
        ),

        "last_feed_ingest_at": (
            latest_feed_ingest.last_ingested_at
            if latest_feed_ingest
            else None
        ),
    }
