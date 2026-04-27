from fastapi import APIRouter

router = APIRouter()


@router.get("/articles")
def list_articles():
    return {
        "articles": [
            {
                "id": 1,
                "title": "SignalStack first mock article",
                "source": "Example RSS",
                "url": "https://example.com/article-1",
            }
        ]
    }
