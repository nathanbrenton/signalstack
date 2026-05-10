"""add ml category to articles

Revision ID: 21066a3272af
Revises: 49d06ee78363
Create Date: 2026-05-09 23:36:11.663025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21066a3272af'
down_revision: Union[str, Sequence[str], None] = '49d06ee78363'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "articles",
        sa.Column("ml_category", sa.String(length=100), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("articles", "ml_category")
