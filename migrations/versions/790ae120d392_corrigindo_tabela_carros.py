"""Corrigindo Tabela Carros

Revision ID: 790ae120d392
Revises: f84e956a2ced
Create Date: 2024-05-08 21:33:25.463579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '790ae120d392'
down_revision: Union[str, None] = 'f84e956a2ced'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
