from datetime import datetime

from sqlalchemy.orm import Session

from app.ingestion.fetch_rss import ingest_feed
from app.models.rss_feed_source import RSSFeedSource
from app.services.rss_feed_sources import sync_rss_feed_sources


def ingest_active_rss_feeds(db: Session) -> dict:
    sync_result = sync_rss_feed_sources(db)

    active_sources = (
        db.query(RSSFeedSource)
        .filter(RSSFeedSource.is_active.is_(True))
        .order_by(RSSFeedSource.id)
        .all()
    )

    processed_count = 0
    success_count = 0
    error_count = 0
    errors = []

    for source in active_sources:
        processed_count += 1

        try:
            ingest_feed(db, source.url)

            source.last_ingested_at = datetime.utcnow()
            source.last_error = None

            success_count += 1

        except Exception as exc:
            source.last_error = str(exc)
            error_count += 1

            errors.append(
                {
                    "url": source.url,
                    "error": str(exc),
                }
            )

        db.commit()

    return {
        "sync": sync_result,
        "processed_count": processed_count,
        "success_count": success_count,
        "error_count": error_count,
        "errors": errors,
    }
