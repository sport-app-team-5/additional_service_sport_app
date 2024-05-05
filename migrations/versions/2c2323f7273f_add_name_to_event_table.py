"""add name to event table

Revision ID: 2c2323f7273f
Revises: 7a7c9d6b264b
Create Date: 2024-05-02 13:28:06.364826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c2323f7273f'
down_revision: Union[str, None] = '7a7c9d6b264b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('event', sa.Column('name', sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column('event', 'name')
