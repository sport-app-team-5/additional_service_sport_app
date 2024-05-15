"""add category food and allergies

Revision ID: f4f468708937
Revises: 933f86ea599f
Create Date: 2024-05-14 22:43:39.081412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4f468708937'
down_revision: Union[str, None] = '933f86ea599f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('products', sa.Column('allergies', sa.String, nullable=True))
    op.add_column('products', sa.Column('category_food', sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column('products', 'allergies')
    op.drop_column('products', 'category_food')
