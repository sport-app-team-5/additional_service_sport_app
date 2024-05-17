"""create table Notification for service - sportman notifications

Revision ID: b947c0f4c55d
Revises: 1d92bea9220a
Create Date: 2024-05-16 16:51:32.273539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b947c0f4c55d'
down_revision: Union[str, None] = '1d92bea9220a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'notification',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.String(30)),
        sa.Column('type', sa.String(30)),
        sa.Column('status', sa.String(30)),
        sa.Column('created_at', sa.DateTime, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now())  
              
    )


def downgrade() -> None:
    op.drop_table('notification')
