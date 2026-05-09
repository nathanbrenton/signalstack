"""convert search vector to tsvector

Revision ID: 96276662b374
Revises: 236f0a21245c
Create Date: 2026-05-07 18:59:16.371969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '96276662b374'
down_revision: Union[str, Sequence[str], None] = '236f0a21245c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_articles_search_vector_gin;")

    op.execute(
        """
        ALTER TABLE articles
        ALTER COLUMN search_vector
        TYPE tsvector
        USING to_tsvector('english', search_vector);
        """
    )

    op.execute(
        """
        CREATE INDEX ix_articles_search_vector_gin
        ON articles
        USING gin (search_vector);
        """
    )

def downgrade() -> None:
    op.execute("DROP INDEX ix_articles_search_vector_gin;")

    op.execute(
        """
        ALTER TABLE articles
        ALTER COLUMN search_vector
        TYPE varchar
        USING search_vector::text;
        """
    )

    op.execute(
        """
        CREATE INDEX ix_articles_search_vector_gin
        ON articles
        USING gin (to_tsvector('english', search_vector));
        """
    )
