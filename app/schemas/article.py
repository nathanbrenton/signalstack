from datetime import datetime
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    url: str
    summary: str | None = None
    published_at: datetime | None = None
    source_name: str | None = None
#    source: str | None = None
#    content: str | None = None


class ArticleCreate(ArticleBase):
    pass


class ArticleRead(ArticleBase):
    id: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True
