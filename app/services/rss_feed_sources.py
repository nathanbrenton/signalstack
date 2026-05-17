from sqlalchemy.orm import Session

from app.config.rss_feeds import RSS_FEEDS
from app.models.rss_feed_source import RSSFeedSource


def sync_rss_feed_sources(db: Session) -> dict:
    configured_urls = set(RSS_FEEDS)

    existing_sources = db.query(RSSFeedSource).all()

    existing_by_url = {
        source.url: source
        for source in existing_sources
    }

    created_count = 0
    activated_count = 0
    deactivated_count = 0

    for url in configured_urls:
        source = existing_by_url.get(url)

        if source is None:
            db.add(
                RSSFeedSource(
                    url=url,
                    is_active=True,
                )
            )

            created_count += 1

        elif not source.is_active:
            source.is_active = True
            source.last_error = None
            activated_count += 1

    for source in existing_sources:
        if source.url not in configured_urls and source.is_active:
            source.is_active = False
            deactivated_count += 1

    db.commit()

    return {
        "configured_count": len(configured_urls),
        "created_count": created_count,
        "activated_count": activated_count,
        "deactivated_count": deactivated_count,
    }
