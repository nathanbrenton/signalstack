"""add ml confidence to articles

Revision ID: fab09bff5fb5
Revises: 21066a3272af
Create Date: 2026-05-10 03:30:30.148462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fab09bff5fb5'
down_revision: Union[str, Sequence[str], None] = '21066a3272af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "articles",
        sa.Column(
            "ml_confidence",
            sa.Float(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "articles",
        "ml_confidence",
    )
