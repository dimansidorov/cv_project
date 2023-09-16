"""Updated column "name" of Type

Revision ID: 1ab43be5040e
Revises: 2c7108eaaa88
Create Date: 2023-09-16 12:54:41.576235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ab43be5040e'
down_revision: Union[str, None] = '2c7108eaaa88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'types', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'types', type_='unique')
    # ### end Alembic commands ###