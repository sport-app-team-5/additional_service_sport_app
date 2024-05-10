"""Add is inside house in service table

Revision ID: a4cb22eadbfc
Revises: 2c2323f7273f, 6a6e2e508cc9
Create Date: 2024-05-07 10:10:33.984842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4cb22eadbfc'
down_revision: Union[str, None] = ('2c2323f7273f', '6a6e2e508cc9')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('service', sa.Column('is_inside_house', sa.Boolean, nullable=True))


def downgrade() -> None:
    op.drop_column('service', 'is_inside_house')
