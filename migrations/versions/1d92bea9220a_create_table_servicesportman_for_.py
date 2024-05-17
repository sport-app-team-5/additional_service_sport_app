"""create table ServiceSportman for service - sportman appointments

Revision ID: 1d92bea9220a
Revises: a4cb22eadbfc
Create Date: 2024-05-16 15:47:51.701130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1d92bea9220a'
down_revision: Union[str, None] = 'a4cb22eadbfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'service_sportman',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('service_id', sa.Integer, sa.ForeignKey("service.id"), index=True),
        sa.Column('sportman_id', sa.Integer),
        sa.Column('sport', sa.String(30)),
        sa.Column('injury_id', sa.Integer),
        sa.Column('appointment_date', sa.String(30)),
        sa.Column('created_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime, default=sa.text('CURRENT_TIMESTAMP'), onupdate=sa.text('CURRENT_TIMESTAMP'))
    )

def downgrade() -> None:
    op.drop_table('service_sportman')
