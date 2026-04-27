from fastapi import APIRouter
from app.api.v1.endpoints import articles, health

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(articles.router, tags=["articles"])
