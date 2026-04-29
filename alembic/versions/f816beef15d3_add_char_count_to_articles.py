"""add char_count to articles

Revision ID: f816beef15d3
Revises: 695ab6200d50
Create Date: 2026-04-28 18:58:13.943497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f816beef15d3'
down_revision: Union[str, Sequence[str], None] = '695ab6200d50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "articles",
        sa.Column("char_count", sa.Integer(), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("articles", "char_count")
