from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
)

app.include_router(api_router, prefix="/api/v1")

app.mount("/demo", StaticFiles(directory="app/static", html=True), name="static")


@app.get("/")
def read_root():
    return {
        "message": f"{settings.APP_NAME} is running",
        "environment": settings.ENV,
    }
