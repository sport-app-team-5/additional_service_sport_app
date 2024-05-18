"""merge D and F

Revision ID: 933f86ea599f
Revises: 2c2323f7273f, 6a6e2e508cc9
Create Date: 2024-05-14 22:43:09.735925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '933f86ea599f'
down_revision: Union[str, None] = ('2c2323f7273f', '6a6e2e508cc9')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
