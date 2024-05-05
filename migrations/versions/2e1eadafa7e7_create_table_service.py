"""Create table Service

Revision ID: 2e1eadafa7e7
Revises: 76795f3c6fde
Create Date: 2024-04-12 21:56:19.993816

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2e1eadafa7e7'
down_revision: Union[str, None] = '76795f3c6fde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'service',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('third_party_id', sa.Integer(), sa.ForeignKey('third_party.id'), index=True),
        sa.Column('type', sa.String(30), nullable=False),
        sa.Column('description', sa.String(512), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('cost', sa.Double, nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow, nullable=False),
        sa.Column('updated_at', sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('service')
