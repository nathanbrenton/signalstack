"""add ml classification timestamp

Revision ID: 37ef7f3c97da
Revises: fab09bff5fb5
Create Date: 2026-05-12 23:10:22.552530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37ef7f3c97da'
down_revision: Union[str, Sequence[str], None] = 'fab09bff5fb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "articles",
        sa.Column(
            "ml_last_classified_at",
            sa.DateTime(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "articles",
        "ml_last_classified_at",
    )
