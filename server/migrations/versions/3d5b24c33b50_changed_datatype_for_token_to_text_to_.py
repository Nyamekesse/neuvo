"""changed datatype for token to text to store them efficiently in refresh token table

Revision ID: 3d5b24c33b50
Revises: 3380c6522880
Create Date: 2023-04-11 04:20:35.141659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d5b24c33b50'
down_revision = '3380c6522880'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('refresh_token', schema=None) as batch_op:
        batch_op.alter_column('token',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('refresh_token', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('token',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###
