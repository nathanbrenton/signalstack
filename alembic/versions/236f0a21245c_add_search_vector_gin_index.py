"""add search vector gin index

Revision ID: 236f0a21245c
Revises: dccea5522687
Create Date: 2026-05-07 09:33:21.214858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '236f0a21245c'
down_revision: Union[str, Sequence[str], None] = 'dccea5522687'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE INDEX ix_articles_search_vector_gin "
        "ON articles USING gin (to_tsvector('english', search_vector));"
    )


def downgrade() -> None:
    op.execute("DROP INDEX ix_articles_search_vector_gin;")
