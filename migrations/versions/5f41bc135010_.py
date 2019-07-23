"""empty message

Revision ID: 5f41bc135010
Revises: 9c4e9be63054
Create Date: 2019-07-19 13:42:21.537476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f41bc135010'
down_revision = '9c4e9be63054'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('status', sa.String(length=255), nullable=False))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('car', 'status')
    # ### end Alembic commands ###