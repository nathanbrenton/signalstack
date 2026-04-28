from datetime import datetime
from app.db.session import SessionLocal
from app.models.article import Article
import feedparser


RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"


def main():
    db = SessionLocal()

    try:
        feed = feedparser.parse(RSS_URL)
        source_name = feed.feed.get("title")

        print(f"Feed title: {feed.feed.get('title')}")
        print(f"Entries found: {len(feed.entries)}")

        for entry in feed.entries[:5]: # change number here to test (e.g. 1)
            title = entry.get("title")
            url = entry.get("link")

#            print(entry.keys())
#            published = entry.get("published")
#            print(f"Published: {published}")
            published_parsed = entry.get("published_parsed")

            published_at = None
            if published_parsed:
                published_at = datetime(*published_parsed[:6])

            print(f"Published at: {published_at}")
            print(f"Source: {source_name}")


            if not title or not url:
                print("Skipping invalid entry")
                continue

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

    finally:
        db.close()


if __name__ == "__main__":
    main()
