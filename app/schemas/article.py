from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    url: str
    source: str | None = None
    content: str | None = None


class ArticleCreate(ArticleBase):
    pass


class ArticleRead(ArticleBase):
    id: int

    class COnfig:
        from_attributes = True
