from fastapi import APIRouter
from app.api.v1.endpoints import (
    articles,
    health,
    ml,
    ml_health,
    rss_feeds,
)

api_router = APIRouter()

# REGISTER
api_router.include_router(health.router, tags=["health"])
api_router.include_router(articles.router, tags=["articles"])
api_router.include_router(ml.router, tags=["ml"])
api_router.include_router(ml_health.router, tags=["ml"])
api_router.include_router(rss_feeds.router, tags=["rss-feeds"])
