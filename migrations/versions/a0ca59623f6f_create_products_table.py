"""create products table

Revision ID: a0ca59623f6f
Revises: 2e1eadafa7e7
Create Date: 2024-04-16 11:50:22.857901

"""
from datetime import datetime
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0ca59623f6f'
down_revision: Union[str, None] = '2e1eadafa7e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('third_party_id', sa.Integer(), sa.ForeignKey('third_party.id'), index=True),
        sa.Column('category', sa.String(30), nullable=False),
        sa.Column('description', sa.String(512), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('cost', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow, nullable=False),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('products')
