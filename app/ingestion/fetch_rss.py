from datetime import datetime
from app.config.rss_feeds import RSS_FEEDS
from app.db.session import SessionLocal
from app.models.article import Article
import feedparser


#RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"
#RSS_FEEDS = [
#    "https://feeds.bbci.co.uk/news/world/rss.xml",
#    "https://www.aljazeera.com/xml/rss/all.xml",
#]


def ingest_feed(db, rss_url):
    feed = feedparser.parse(rss_url)
    source_name = feed.feed.get("title")

    print(f"Feed title: {source_name}")
    print(f"Entries found: {len(feed.entries)}")

    for entry in feed.entries[:5]:
        title = entry.get("title")
        url = entry.get("link")

        if not title or not url:
            print("Skipping invalid entry")
            continue

        published_parsed = entry.get("published_parsed")

        published_at = None
        if published_parsed:
            published_at = datetime(*published_parsed[:6])

        print(f"Published at: {published_at}")
        print(f"Source: {source_name}")

        existing_article = db.query(Article).filter(Article.url == url).first()

        if existing_article:
            print(f"Skipping duplicate: {title}")
            continue

        print(f"Inserting: {title}")

        article = Article(
            title=title,
            url=url,
            published_at=published_at,
            source_name=source_name,
        )

        db.add(article)
        db.commit()
        db.refresh(article)

        print(f"Inserted ID: {article.id}")

def main():
    db = SessionLocal()

    try:
        for rss_url in RSS_FEEDS:
            print()
            print(f"Processing feed: {rss_url}")
            ingest_feed(db, rss_url)

    finally:
        db.close()


if __name__ == "__main__":
    main()
