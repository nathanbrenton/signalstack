from fastapi import APIRouter
from app.api.v1.endpoints import (
    articles,
    health,
    ml,
    ml_health,
)

api_router = APIRouter()

# REGISTER
api_router.include_router(health.router, tags=["health"])
api_router.include_router(articles.router, tags=["articles"])
api_router.include_router(ml.router)
api_router.include_router(ml_health.router)
