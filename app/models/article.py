from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.db.base import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False, index=True)
    summary = Column(String, nullable=True)
    clean_summary = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)
    source_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
