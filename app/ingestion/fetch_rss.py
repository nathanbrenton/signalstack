from datetime import datetime
from app.config.rss_feeds import RSS_FEEDS, INGEST_LIMIT
from app.db.session import SessionLocal
from app.models.article import Article
from app.utils.text_cleaning import (
    clean_html_summary,
    create_summary_hash,
    detect_language,
    extract_keywords,
    normalize_title,
)
import feedparser


#RSS_URL = "https://feeds.bbci.co.uk/news/world/rss.xml"
#RSS_FEEDS = [
#    "https://feeds.bbci.co.uk/news/world/rss.xml",
#    "https://www.aljazeera.com/xml/rss/all.xml",
#]


def ingest_feed(db, rss_url):
    feed = feedparser.parse(rss_url)
    if feed.bozo:
        raise Exception(f"Malformed feed or parse error: {feed.bozo_exception}")

    source_name = feed.feed.get("title")

    print(f"Feed title: {source_name}")
    print(f"Entries found: {len(feed.entries)}")

    for entry in feed.entries[:INGEST_LIMIT]:
        title = entry.get("title")
        normalized_title = normalize_title(title)
        url = entry.get("link")
#        summary = clean_html_summary(entry.get("summary"))
        raw_summary = entry.get("summary")
        language = detect_language(raw_summary)
        clean_summary, tokens = clean_html_summary(raw_summary)
        summary_hash = create_summary_hash(clean_summary)
        word_count = len(raw_summary.split()) if raw_summary else 0
        char_count = len(clean_summary) if clean_summary else 0
        token_count = len(tokens)
        keywords = extract_keywords(tokens)
        keywords_text = ", ".join(keywords)
        top_keyword = keywords[0] if keywords else None


        if not title or not url:
            print("Skipping invalid entry")
            continue

        published_parsed = entry.get("published_parsed")

        published_at = None
        if published_parsed:
            published_at = datetime(*published_parsed[:6])

        print(f"Published at: {published_at}")
        print(f"Source: {source_name}")
        print(f"Clean summary: {clean_summary[:100] if clean_summary else None}") # for debugging only

#        existing_article = db.query(Article).filter(Article.url == url).first()
        existing_article = (
            db.query(Article)
            .filter(
                (Article.url == url)
                | (
                    Article.summary_hash == summary_hash
                    if summary_hash
                    else False
                )
                | (
                    Article.normalized_title == normalized_title
                    if normalized_title
                    else False
                )
            )
            .first()
        )

        if existing_article:
            print(f"Skipping duplicate: {title}")
            continue

        print(f"Inserting: {title}")

        ingested_at = datetime.utcnow()

        article = Article(
            title=title,
            normalized_title=normalized_title,
            url=url,
            summary=raw_summary,
            summary_hash=summary_hash,
            clean_summary=clean_summary,
            word_count=word_count,
            char_count=char_count,
            published_at=published_at,
            language=language,
            source_name=source_name,
            token_count=token_count,
            keywords=keywords_text,
            top_keyword=top_keyword,
            ingested_at=ingested_at,
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

            try:
                ingest_feed(db, rss_url)
            except Exception as exc:
                print(f"Error processing feed: {rss_url}")
                print(f"Reason: {exc}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
