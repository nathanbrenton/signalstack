from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.rss_feeds import RSS_FEEDS
from app.db.deps import get_db
from app.services.rss_feed_sources import sync_rss_feed_sources
from app.services.rss_ingestion import ingest_active_rss_feeds

router = APIRouter()


@router.get("/rss-feeds")
def list_rss_feeds():
    return {
        "count": len(RSS_FEEDS),
        "feeds": RSS_FEEDS,
    }


@router.post("/rss-feeds/sync")
def sync_rss_feeds(db: Session = Depends(get_db)):
    return sync_rss_feed_sources(db)


@router.post("/rss-feeds/ingest")
def ingest_rss_feeds(db: Session = Depends(get_db)):
    return ingest_active_rss_feeds(db)
