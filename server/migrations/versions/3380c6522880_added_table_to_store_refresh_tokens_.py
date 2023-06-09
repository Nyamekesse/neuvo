"""added table to store refresh tokens generated

Revision ID: 3380c6522880
Revises: e3415037cd6d
Create Date: 2023-04-11 04:06:54.464847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3380c6522880'
down_revision = 'e3415037cd6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refresh_token',
    sa.Column('id', sa.String(length=22), nullable=False),
    sa.Column('user_id', sa.String(length=36), nullable=False),
    sa.Column('token', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refresh_token')
    # ### end Alembic commands ###
