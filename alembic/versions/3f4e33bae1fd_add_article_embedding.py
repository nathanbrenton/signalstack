"""add article embedding

Revision ID: 3f4e33bae1fd
Revises: 37ef7f3c97da
Create Date: 2026-05-15 23:14:29.781562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f4e33bae1fd'
down_revision: Union[str, Sequence[str], None] = '37ef7f3c97da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "articles",
        sa.Column(
            "embedding",
            sa.JSON(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "articles",
        "embedding",
    )
