"""add word_count to articles

Revision ID: 695ab6200d50
Revises: a2a4c21f6c20
Create Date: 2026-04-28 18:17:38.113026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '695ab6200d50'
down_revision: Union[str, Sequence[str], None] = 'a2a4c21f6c20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "articles",
        sa.Column("word_count", sa.Integer(), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("articles", "word_count")
