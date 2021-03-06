"""empty message

Revision ID: 6443c509860a
Revises: a13c6e1d693f
Create Date: 2019-02-18 21:04:20.134228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6443c509860a'
down_revision = 'a13c6e1d693f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
