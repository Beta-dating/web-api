"""Check 316e62d7e5ab26da97603755ce0119545e6e221b commit

Revision ID: c3da229ef15e
Revises: cf659f2d1980
Create Date: 2024-06-01 10:19:40.080013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3da229ef15e'
down_revision: Union[str, None] = 'cf659f2d1980'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('form', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.alter_column('form', 'user_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False)
    op.create_unique_constraint(None, 'form', ['user_id'])
    op.add_column('user', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    op.alter_column('user', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('user_id_seq'::regclass)"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('user_id_seq'::regclass)"))
    op.drop_column('user', 'created_at')
    op.drop_constraint(None, 'form', type_='unique')
    op.alter_column('form', 'user_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.drop_column('form', 'created_at')
    # ### end Alembic commands ###