"""create event and sport tables

Revision ID: 7a7c9d6b264b
Revises: a0ca59623f6f
Create Date: 2024-04-23 22:25:30.247689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7a7c9d6b264b'
down_revision: Union[str, None] = 'a0ca59623f6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'sport',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('code', sa.String(5), unique=True),
        sa.Column('name', sa.String(50), unique=True),
        sa.Column('created_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP'),
                  onupdate=sa.text('CURRENT_TIMESTAMP'))
    )

    op.create_table(
        'event',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('third_party_id', sa.Integer, sa.ForeignKey('third_party.id'), index=True),
        sa.Column('city_id', sa.Integer),
        sa.Column('sport_id', sa.Integer, sa.ForeignKey('sport.id'), index=True),
        sa.Column('location', sa.String(150)),
        sa.Column('date', sa.String(30)),
        sa.Column('capacity', sa.Integer),
        sa.Column('description', sa.String(256)),
        sa.Column('type', sa.String(30)),
        sa.Column('created_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP'),
                  onupdate=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade():
    op.drop_table('event')
    op.drop_table('sport')
