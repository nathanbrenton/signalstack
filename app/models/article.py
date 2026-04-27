from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False, index=True)
    source = Column(String, nullable=True)
    content = Column(Text, nullable=True)

