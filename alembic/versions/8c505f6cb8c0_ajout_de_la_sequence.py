"""Ajout de la sequence

Revision ID: 8c505f6cb8c0
Revises: ee840485863f
Create Date: 2024-11-13 16:22:18.255410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c505f6cb8c0'
down_revision: Union[str, None] = 'ee840485863f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'tenant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'tenant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###