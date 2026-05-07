from datetime import datetime
from pydantic import BaseModel

# Article response schema
class ArticleBase(BaseModel):
    title: str
    url: str
    summary: str | None = None
    clean_summary: str | None = None
    published_at: datetime | None = None
    source_name: str | None = None
    word_count: int | None = None
    char_count: int | None = None
    normalized_title: str | None = None
    summary_hash: str | None = None
    keywords: str | None = None
    top_keyword: str | None = None
    language: str | None = None
    token_count: int | None = None
    ingested_at: datetime | None = None
    quality_score: float | None = None


class ArticleCreate(ArticleBase):
    pass


class ArticleRead(ArticleBase):
    id: int
    rank: float | None = None
    created_at: datetime | None = None

    class Config:
        from_attributes = True


class ArticleListMeta(BaseModel):
    page: int
    limit: int
    total: int
    pages: int


class ArticleListResponse(BaseModel):
    data: list[ArticleRead]
    meta: ArticleListMeta
