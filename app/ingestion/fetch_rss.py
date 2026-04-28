from app.db.session import SessionLocal
from app.models.article import Article
import feedparser


RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"


def main():
    db = SessionLocal()

    try:
        feed = feedparser.parse(RSS_URL)

        print(f"Feed title: {feed.feed.get('title')}")
        print(f"Entries found: {len(feed.entries)}")

        for entry in feed.entries[:5]: # ONLY 1 for now
            title = entry.get("title")
            url = entry.get("link")

            existing_article = db.query(Article).filter(Article.url == url).first()

            if existing_article:
                print(f"Skipping duplicate: {title}")
                continue

            print(f"Inserting: {title}")

            article = Article(
                title=title,
                url=url
            )

            db.add(article)
            db.commit()
            db.refresh(article)

            print(f"Inserted ID: {article.id}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
