"""fix search vector gin index

Revision ID: 49d06ee78363
Revises: 96276662b374
Create Date: 2026-05-08 21:17:33.158189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49d06ee78363'
down_revision: Union[str, Sequence[str], None] = '96276662b374'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_articles_search_vector_gin;")
    op.execute(
        "CREATE INDEX ix_articles_search_vector_gin "
        "ON articles USING gin (search_vector);"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_articles_search_vector_gin;")
    op.execute(
        "CREATE INDEX ix_articles_search_vector_gin "
        "ON articles USING gin (to_tsvector('english', search_vector));"
    )
