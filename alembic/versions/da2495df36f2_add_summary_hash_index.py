"""add summary_hash index

Revision ID: da2495df36f2
Revises: 9785239653db
Create Date: 2026-04-29 10:10:53.205910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da2495df36f2'
down_revision: Union[str, Sequence[str], None] = '9785239653db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
op.create_index(
    "ix_articles_summary_hash",
    "articles",
    ["summary_hash"],
)

def downgrade() -> None:
    """Downgrade schema."""
op.drop_index(
    "ix_articles_summary_hash",
    table_name="articles",
)

