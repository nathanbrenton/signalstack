from app.db.session import SessionLocal
from app.ml.inference import predict_article_category
from app.models.article import Article


def main():
    db = SessionLocal()

    try:
        articles = (
            db.query(Article)
            .filter(Article.ml_confidence.is_(None))
            .all()
        )

        print(f"Articles needing ML confidence: {len(articles)}")

        updated_count = 0

        for article in articles:
            text = " ".join(
                value
                for value in [
                    article.title,
                    article.clean_summary,
                    article.summary,
                ]
                if value
            )

            if not text:
                continue

            category, confidence = predict_article_category(text)

            article.ml_category = category
            article.ml_confidence = confidence

            updated_count += 1

        db.commit()

        print(f"Updated articles: {updated_count}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
