"""create table EventSportman for events - sportman subscription

Revision ID: 6a6e2e508cc9
Revises: 7a7c9d6b264b
Create Date: 2024-05-04 13:19:01.753735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a6e2e508cc9'
down_revision: Union[str, None] = '7a7c9d6b264b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'event_sportman',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('event_id', sa.Integer, sa.ForeignKey('event.id'), index=True),
        sa.Column('sportman_id', sa.Integer),
        sa.Column('created_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP'), onupdate=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade() -> None:
    op.drop_table('event_sportman')
